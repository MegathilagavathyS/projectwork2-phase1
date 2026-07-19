Adaptive Image Enhancement for Explainable Glaucoma Detection Using Deep Learning
Problem Statement
Introduction

Glaucoma is one of the leading causes of irreversible blindness worldwide. It is an eye disease that damages the optic nerve due to increased intraocular pressure or other factors. Since glaucoma develops gradually without noticeable symptoms in its early stages, many patients lose vision before realizing they have the disease. According to the World Health Organization (WHO), glaucoma is the second leading cause of blindness globally. Early detection and timely treatment can slow down or prevent further vision loss.

Currently, glaucoma diagnosis is performed by ophthalmologists through retinal fundus image examination and other clinical tests. However, manual screening is time-consuming, requires experienced specialists, and is not easily accessible in rural or resource-limited areas. Therefore, there is a need for an intelligent, automated, and explainable glaucoma detection system that can assist doctors in making faster and more reliable decisions.

Existing Problem

Current glaucoma detection systems have several limitations:

Manual diagnosis requires experienced ophthalmologists.
Screening large numbers of retinal images is time-consuming.
Most deep learning models apply the same preprocessing technique to every retinal image.
Poor-quality retinal images reduce detection accuracy.
Existing AI models often act as "black boxes" with limited explainability.
Most systems only predict whether glaucoma is present and provide limited decision support.

Most existing research focuses on:

CNN-based glaucoma detection
Transfer learning using pre-trained models
Basic image preprocessing
Optic disc and optic cup segmentation
Binary glaucoma classification

However, very few systems focus on adaptive image enhancement based on image quality before classification.

Problem Definition

The objective of this project is to develop an Explainable Deep Learning-based Glaucoma Detection System that accurately detects glaucoma from retinal fundus images using adaptive image enhancement and Explainable Artificial Intelligence (XAI).

The proposed system aims to answer the following question:

"Does this retinal image indicate glaucoma, and why did the AI make this prediction?"

Proposed Solution

The proposed system introduces an Adaptive Image Enhancement Pipeline that first analyzes the quality of the retinal fundus image and automatically selects the most suitable preprocessing technique.

Based on image characteristics:

CLAHE is applied to low-contrast images.
Gamma Correction is applied to dark images.
Bilateral Filtering is applied to noisy images.
Unsharp Masking is applied to blurred images.
Good-quality images are processed without unnecessary enhancement.

The enhanced retinal image is then provided as input to the EfficientNet-B3 deep learning model for glaucoma detection.

To improve transparency, Grad-CAM++ is integrated to highlight the retinal regions responsible for the prediction. The system also generates a confidence score and a simple clinical recommendation to support ophthalmologists.

Input Parameters
Retinal Image Parameters
Fundus retinal image
Image brightness
Image contrast
Image sharpness
Noise level
Extracted Retinal Features

The model automatically learns important retinal features such as:

Optic Disc
Optic Cup
Cup-to-Disc Ratio
Blood Vessel Pattern
Retinal Texture
System Output

The proposed system provides:

Glaucoma Prediction

Example:

Prediction: Glaucoma Detected

or

Prediction: Normal Eye

Confidence Score

Example:

Confidence: 97%

Explainable AI Visualization

Grad-CAM++ heatmap highlighting the retinal regions responsible for glaucoma detection.

Clinical Recommendation

Example:

Prediction: Glaucoma Detected
Confidence: 97%
Highlighted optic nerve region
Recommendation: Consult an ophthalmologist for further clinical evaluation.
Objectives

The main objectives of this project are:

To develop a deep learning model for accurate glaucoma detection.
To improve retinal image quality using adaptive image enhancement.
To reduce the effect of poor-quality retinal images.
To provide explainable predictions using Grad-CAM++.
To generate confidence-aware predictions.
To support ophthalmologists in early glaucoma diagnosis.
Deep Learning Approach
EfficientNet-B3

EfficientNet-B3 is selected because it provides:

High classification accuracy.
Lower computational cost.
Faster training using transfer learning.
Better performance on medical image datasets.
Adaptive Image Enhancement

Instead of applying the same preprocessing to every image, the system first evaluates image quality.

Depending on the image condition:

Low Contrast → CLAHE
Dark Image → Gamma Correction
Noisy Image → Bilateral Filter
Blurred Image → Unsharp Masking
Good Image → No preprocessing

This adaptive approach improves image quality before classification.

System Workflow
Fundus Retinal Image
        │
        ▼
Image Quality Analysis
        │
        ▼
Adaptive Image Enhancement
(CLAHE / Gamma Correction /
Bilateral Filter /
Unsharp Masking)
        │
        ▼
Image Normalization
        │
        ▼
EfficientNet-B3
        │
        ▼
Glaucoma Prediction
        │
        ▼
Grad-CAM++
        │
        ▼
Confidence Score
        │
        ▼
Clinical Recommendation
Scope of the Project

The proposed system can be used in:

Hospitals
Eye Care Clinics
Ophthalmology Centers
Rural Healthcare Centers
Telemedicine Platforms
Vision Screening Programs
Semester 2 Extension

The system can later be extended with:

Clinical decision support dashboard.
Patient history management.
Disease progression monitoring.
Mobile application for glaucoma screening.
Multi-eye disease detection (Glaucoma + Diabetic Retinopathy + Cataract).
Innovation

Unlike traditional glaucoma detection systems, the proposed project introduces:

Adaptive Image Enhancement based on image quality.
Explainable AI using Grad-CAM++.
Confidence-aware prediction.
Automatic clinical recommendation.
Evaluation across multiple public glaucoma datasets (ACRIMA, ORIGA, RIM-ONE DL, and PAPILA).

These innovations improve the reliability, transparency, and clinical usefulness of glaucoma screening.

Datasets Used
Dataset	Purpose
ACRIMA	Main training dataset
ORIGA	Additional training and validation
RIM-ONE DL	Independent testing
PAPILA	External validation

These publicly available datasets provide approximately 2,300 retinal fundus images, which are sufficient for training, validation, and testing.

Technologies Used
Python
TensorFlow / Keras
OpenCV
Scikit-learn
EfficientNet-B3
Grad-CAM++
Flask
HTML
CSS
JavaScript
Google Colab
GitHub
Expected Outcome

The developed system will provide an intelligent and explainable platform for early glaucoma detection.

Expected benefits include:

Improved glaucoma detection accuracy.
Better retinal image quality through adaptive enhancement.
Reliable and explainable predictions.
Faster screening process.
Reduced dependence on manual diagnosis.
Support for early treatment and prevention of vision loss.
Conclusion

The proposed Adaptive Image Enhancement for Explainable Glaucoma Detection Using Deep Learning system provides an AI-driven solution for accurate and reliable glaucoma screening. By combining adaptive image enhancement, EfficientNet-B3, and Explainable AI (Grad-CAM++), the system improves detection performance while making predictions transparent and understandable. This intelligent approach can assist ophthalmologists in early diagnosis, reduce the risk of blindness, and improve the quality of eye healthcare.