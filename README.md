# Explainable Diabetic Retinopathy Detection with Adaptive Image Enhancement

## 📖 Project Description

**Explainable Diabetic Retinopathy Detection with Adaptive Image Enhancement** is a deep learning-based medical image analysis project designed to detect different stages of diabetic retinopathy from retinal fundus images. The project aims to improve the accuracy and reliability of diabetic retinopathy diagnosis by introducing an **Adaptive Image Enhancement Pipeline**, **Multi-View Retinal Feature Learning**, and **Explainable Artificial Intelligence (XAI)**.

Unlike conventional approaches that apply the same preprocessing technique to every retinal image, the proposed system first analyzes the quality of the input image and automatically selects the most suitable enhancement method. Depending on the image characteristics, techniques such as **CLAHE**, **Gamma Correction**, **Unsharp Masking**, or **Bilateral Filtering** are applied to improve image quality while preserving important retinal features.

After enhancement, the retinal image is converted into multiple representations, including the **Original RGB Image**, **Green Channel Image**, and **CLAHE-Enhanced Image**. These multiple views capture complementary information about blood vessels, microaneurysms, hemorrhages, and other retinal abnormalities. The extracted features are combined and provided as input to an **EfficientNet-B0** deep learning model for accurate five-class diabetic retinopathy classification.

To improve the transparency of the prediction, the project integrates **Grad-CAM++**, which highlights the retinal regions responsible for the model's decision. The system also generates a **confidence score** and a **clinical report**, enabling doctors and healthcare professionals to better understand and trust the model's predictions.

---

# 🎯 Objectives

* Develop an intelligent deep learning model for diabetic retinopathy detection.
* Improve retinal image quality using adaptive image enhancement.
* Extract complementary retinal features using multi-view image representations.
* Classify retinal images into five diabetic retinopathy severity stages.
* Provide explainable predictions using Grad-CAM++.
* Generate confidence-aware predictions and clinical reports.
* Develop a simple web application for diabetic retinopathy screening.

---

# 🚀 Proposed Workflow

```text
Retinal Fundus Image
          │
          ▼
Image Quality Analysis
          │
          ▼
Adaptive Image Enhancement
(CLAHE / Gamma Correction /
Unsharp Masking / Bilateral Filter)
          │
          ▼
Multi-View Image Generation
(RGB + Green Channel + CLAHE)
          │
          ▼
Feature Fusion
          │
          ▼
EfficientNet-B0
          │
          ▼
Five-Class DR Classification
          │
          ▼
Grad-CAM++ Visualization
          │
          ▼
Confidence Score
          │
          ▼
Clinical Report
```

---

# 📂 Dataset

The project uses publicly available retinal fundus image datasets:

* **APTOS 2019 **


The images are categorized into five classes:

* No Diabetic Retinopathy
* Mild
* Moderate
* Severe
* Proliferative Diabetic Retinopathy

---

# 🧠 Deep Learning Model

**Primary Model**

* EfficientNet-B0

**Image Processing Techniques**

* CLAHE
* Gamma Correction
* Unsharp Masking
* Bilateral Filtering

**Explainable AI**

* Grad-CAM++

---

# 🛠 Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Pandas
* Scikit-learn
* Matplotlib
* Flask
* HTML
* CSS
* JavaScript

---

# ✨ Key Features

* Adaptive Image Enhancement
* Multi-View Retinal Feature Learning
* Five-Class Diabetic Retinopathy Classification
* Explainable AI using Grad-CAM++
* Confidence Score Generation
* Clinical Report Generation
* Web-Based Prediction System

---

# 📋 Expected Output

The system provides:

* Predicted Diabetic Retinopathy Stage
* Confidence Score
* Grad-CAM++ Heatmap
* Clinical Report

### Example

**Prediction:** Moderate Diabetic Retinopathy

**Confidence:** 96%

**Recommendation:** Consult an ophthalmologist for further clinical evaluation.

---

# 💡 Project Novelty

The proposed project introduces several innovative features compared to traditional diabetic retinopathy detection systems:

* Adaptive Image Enhancement based on image quality instead of fixed preprocessing.
* Multi-View Retinal Feature Learning using RGB, Green Channel, and CLAHE-enhanced images.
* Explainable AI through Grad-CAM++ for transparent predictions.
* Confidence-aware prediction to improve reliability.
* Automatic clinical report generation to support medical decision-making.

---

# 📌 Expected Deliverables

* Literature Survey
* Dataset Collection
* Adaptive Image Enhancement Module
* Multi-View Image Generation Module
* EfficientNet-B0 Classification Model
* Explainable AI Module (Grad-CAM++)
* Confidence Score Module
* Clinical Report Generation
* Web Application
* Project Documentation

---

# 🔮 Future Scope

* Disease Progression Prediction
* Lesion Detection and Quantification
* Personalized Treatment Recommendation
* Multi-Disease Retinal Screening
* Mobile Application Development
* Cloud Deployment
* Electronic Health Record (EHR) Integration

---

# 📌 Project Title

**Explainable Diabetic Retinopathy Detection with Adaptive Image Enhancement**

**Domain:** Deep Learning | Medical Image Analysis | Computer Vision | Explainable Artificial Intelligence (XAI)
