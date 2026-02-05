
# Team Number – Project Title

## Team Info
- 22471A05B7 — **Karishma** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A05C8 — **Sumiya Shaik** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

- 22471A0577 — **Sowjanya Koduri** ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: xxxxxxxxxx_

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

## Dependencies Used
Python,PyTorch ,Ultralytics,YOLOv8,OpenCV,NumPy,Matplotlib

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
Evaluation Metrics Used:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

Testing showed:

Strong generalization on unseen CT images

High class-wise prediction confidence

Minimal misclassification between similar disease types

---

## Model Testing / Evaluation
Evaluation Metrics Used:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

Testing showed:

Strong generalization on unseen CT images

High class-wise prediction confidence

Minimal misclassification between similar disease types

---

## Results


---

## Limitations & Future Work
Limitations

Dataset limited to a single public source.

No real-time clinical deployment yet.

No ensemble or attention-based architecture in current version.

Future Work

Validate on multi-center hospital datasets

Apply K-Fold Cross Validation

Integrate attention mechanisms (SE / CBAM)

Explore ensemble learning (YOLOv8 + CNN / Transformer)

Optimize for mobile and edge-device deployment

Conduct clinical trials with radiologist comparison

---

## Deployment Info
xxxxxxxxxx

---
