
# Team Number – A Deep Learning Model for Automated Kidney Disease Classification Using CT Imaging.

## Team Info
- 22471A05B7 — **Karishma** ( [LinkedIn](https://www.linkedin.com/in/karishmapathan115866276/))
_Work Done: Model training, evaluation, preprocessing

- 22471A05C8 — **Sumiya Shaik** ( [LinkedIn](https://www.linkedin.com/in/sumiya-shaik-406106292?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) )
_Work Done:documentation, Dataset preparation

- 22471A0577 — **Sowjanya Koduri** ( [LinkedI(https://www.linkedin.com/in/sowjanyareddy99089/))
_Work Done:Research analysis, testing

---

## Abstract
Abstract—Kidney diseases like stones, cysts, and tumors affect
millions of people worldwide and often go unnoticed until they
reach serious stages. Reading CT scans manually is not only timeconsuming but also vulnerable to human error, which can delay
treatment. To tackle this issue, we built an intelligent diagnostic
framework that can automatically classify kidney CT images
into four categories: normal, cyst, stone, and tumor. At its core is
YOLOv8n-cls, a lightweight deep learning model designed for fast
and efficient image classification. The framework improves CT
scan quality through preprocessing steps—such as resizing, denoising, and contrast enhancement—and boosts reliability using
data augmentation. We trained the model on a balanced dataset
of 18,948 CT images, where it achieved a classification accuracy of
96.88% across all categories. Compared to traditional diagnostic
workflows, our system provides radiologists with quick, accurate,
and reliable assistance, reducing both interpretation time and
diagnostic errors. Thanks to its compact design, it can be deployed in hospitals, local clinics, or even telemedicine platforms,
making it especially useful in low-resource settings. While further
validation on external datasets is needed, this approach shows
strong potential to support early detection and improve patient
outcomes in kidney disease care.

---

## Paper Reference (Inspiration)
Multi-Class Kidney Abnormalities Detecting Novel System Through Computed Tomography.

 – Author Names:[ SAGAR DHANRAJ PANDE,RAGHAV AGARWAL]
 
 (https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10384368)
Original conference/IEEE paper used as inspiration for the model.

---

## Our Improvement Over Existing Paper
Achieved significantly higher accuracy (96–99%) compared to the reference paper.

Employed advanced preprocessing (CLAHE, normalization, augmentation) to enhance lesion visibility and reduce noise.

Addressed class imbalance more effectively through structured dataset splitting and augmentation.

Leveraged transfer learning and fine-tuning to improve generalization.

Demonstrated high performance even on CPU-only systems, proving suitability for low-resource and rural environments.

Provided better class-wise discrimination across Normal, Cyst, Stone, and Tumor categories.

Focused on classification robustness, not just fast inference

---

## About the Project

🔹 What the project does

This project automatically classifies kidney CT images into four categories:

Normal

Kidney Stone

Kidney Cyst

Kidney Tumor

using a deep learning–based YOLOv8 classification model.

🔹 Why it is useful

Manual CT diagnosis is slow, expert-dependent, and error-prone.

Early kidney disease detection can prevent renal failure and save lives.

Hospitals face a shortage of experienced radiologists.

Our system provides fast, accurate, and consistent AI-assisted diagnosis, even in low-resource settings.

🔹 General Project Workflow

CT Image → Preprocessing → Data Augmentation → YOLOv8 Model → Disease Class Output

More clearly:

Input: Kidney CT images

Processing: Noise removal, contrast enhancement, resizing

Model: YOLOv8n-cls with transfer learning

Output: Predicted kidney condition (Normal / Cyst / Stone / Tumor)
---

## Dataset Used
👉 **[CT Kidney Dataset: Normal–Cyst–Tumor–Stone](https://www.kaggle.com/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone)**

**Dataset Details:**
Imaging Type: CT scans

Classes: Normal, Cyst, Stone, Tumor

Data Source: Hospital CT scans (clinical-grade)

Image Variability: Different orientations, contrast levels, and resolutions

Dataset Split:

Training set

Validation set

Test set (balanced across classes)

---

## EDA & Preprocessing

Explored class distribution to detect imbalance.
Resized all CT images to 224 × 224 for model compatibility.
Applied CLAHE to enhance contrast in low-visibility CT regions.
Normalized pixel values for stable training.
Applied data augmentation:
Rotation
Horizontal flipping
Brightness adjustment
Ensured balanced representation across all kidney disease classes.

---

## Model Training Info
---
Base Model: YOLOv8
Optimizer: Ultralytics
Loss Function: CrossEntropyLoss
Epochs: 20
Learning Rate: 2e-5
---

## Model Testing / Evaluation
Accuracy: 96%
Precision: 95.4%
Recall: 94.7%
F1 Score: 95.0%
Confusion matrix generated for all 40 classes

---

## Results
The model successfully classifies visually similar pests and provides accurate treatment suggestions. Compared to CNN-based systems, yoloV8 shows superior generalization and robustness under real-world conditions.

---

## Limitations & Future Work
The proposed YOLOv8n-cls framework is limited by dataset size and variability in CT scan quality across different clinical settings, and it currently performs classification without lesion localization or segmentation. Model performance may be affected when deployed on extremely low-end devices or unseen real-world data distributions. Future work includes expanding multi-center datasets, adding localization and explainable AI modules, optimizing edge deployment, and integrating clinical data to enhance diagnostic reliability and applicability.
 
---

## Deployment Info
The system is currently deployed as a live prototype on Hugging Face Spaces, enabling real-time pest image classification and recommendation through a web-based interface. Users can upload crop images and receive instant AI-driven predictions along with treatment and prevention guidance. The deployment demonstrates practical usability in an online environment, while future plans include optimizing performance for mobile platforms, integrating cloud APIs, and supporting large-scale user access.

---
