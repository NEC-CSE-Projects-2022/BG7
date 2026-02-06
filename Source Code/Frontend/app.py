import os
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image

# === Initialize Flask ===
app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

# === Load YOLO model ===
model_path = os.path.join(os.path.dirname(__file__), "best.pt")
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found: {model_path}")
model = YOLO(model_path)

# === Class Descriptions ===
class_descriptions = {
    "Tumor": {
        "Cause": "Abnormal kidney cell growth due to mutations, smoking, or obesity.",
        "Treatment": "Surgery, targeted therapy, or immunotherapy.",
        "Steps_to_Follow": "Consult oncologist, regular scans, avoid alcohol/smoking.",
        "Diet": "Balanced diet, low salt, avoid processed foods."
    },
    "Stone": {
        "Cause": "Hard mineral deposits from dehydration or high salt diet.",
        "Treatment": "Water intake, medication, or lithotripsy.",
        "Steps_to_Follow": "Drink 3-4L water, avoid oxalate foods.",
        "Diet": "Citrus fruits, low salt, avoid red meat."
    },
    "Cyst": {
        "Cause": "Fluid-filled sacs due to genetics or kidney disease.",
        "Treatment": "Monitor, control BP, dialysis if severe.",
        "Steps_to_Follow": "Ultrasound checkups, manage kidney function.",
        "Diet": "Low sodium, no alcohol, hydration."
    },
    "Normal": {
        "Cause": "Healthy kidney — no abnormality.",
        "Treatment": "None required.",
        "Steps_to_Follow": "Stay active, regular checkups.",
        "Diet": "Balanced diet, low salt, avoid junk."
    }
}

# === Page Routes ===
@app.route("/")
def home(): return render_template("Home.html")

@app.route("/batch")
def batch_page(): return render_template("Batch.html")

@app.route("/upload")
def upload_page(): return render_template("Upload.html")

# === Prediction Logic ===
def process_prediction(image_file):
    # Standard logic for both routes
    image = Image.open(image_file).convert("RGB")
    results = model(image)
    
    pred_index = results[0].probs.top1
    pred_label = results[0].names[pred_index]
    top_conf = results[0].probs.top1conf.item()
    
    CONF_THRESHOLD = 0.7
    ENTROPY_THRESHOLD = 1.0
    all_confs = np.array([float(p) for p in results[0].probs.data])
    entropy = -np.sum(all_confs * np.log(all_confs + 1e-9))
    
    if top_conf < CONF_THRESHOLD or entropy > ENTROPY_THRESHOLD:
        return {
            "pred_label": "Unknown",
            "is_valid": False,
            "description": {
                "Cause": "Unclear image or low confidence.",
                "Treatment": "Try a clearer kidney CT image.",
                "Steps_to_Follow": "Check image quality or dataset.",
                "Diet": "N/A"
            }
        }
    
    return {
        "pred_label": pred_label,
        "is_valid": True,
        "description": class_descriptions.get(pred_label, {})
    }

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    try:
        result = process_prediction(request.files["image"])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predict-batch", methods=["POST"])
def predict_batch():
    if "images" not in request.files:
        return jsonify({"error": "No images uploaded"}), 400
    
    files = request.files.getlist("images")
    results_list = []
    
    for file in files:
        try:
            res = process_prediction(file)
            res["filename"] = file.filename
            results_list.append(res)
        except Exception as e:
            results_list.append({"filename": file.filename, "error": str(e)})
            
    return jsonify(results_list)

@app.errorhandler(404)
def not_found(e): return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)