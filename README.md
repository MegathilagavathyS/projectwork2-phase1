Adaptive Image Enhancement for Explainable Glaucoma Detection Using Deep Learning

📖 Project Description

Adaptive Image Enhancement for Explainable Glaucoma Detection Using Deep Learning is a deep learning-based medical image analysis project designed to automatically detect glaucoma from retinal fundus images. The project aims to improve the accuracy and reliability of glaucoma diagnosis by introducing an Adaptive Image Enhancement Pipeline and Explainable Artificial Intelligence (XAI).

Unlike conventional glaucoma detection systems that apply the same preprocessing technique to every retinal image, the proposed system first analyzes the quality of the input retinal image and automatically selects the most suitable image enhancement technique. Depending on the image characteristics, techniques such as CLAHE, Gamma Caddorrection, Unsharp Masking, and Bilateral Filtering are applied to improve image quality while preserving important retinal structures.

After enhancement, the processed retinal image is provided as input to the EfficientNet-B3 deep learning model. The model automatically learns important glaucoma-related features such as the optic disc, optic cup, cup-to-disc ratio, and surrounding retinal structures to accurately classify the image as Normal or Glaucoma.

To improve the transparency of the prediction, the project integrates Grad-CAM++, which highlights the retinal regions responsible for the model's decision. The system also generates a confidence score and a clinical recommendation, helping ophthalmologists understand and trust the AI's predictions.

🎯 Objectives
Develop an intelligent deep learning model for glaucoma detection.
Improve retinal image quality using adaptive image enhancement.
Automatically detect glaucoma from retinal fundus images.
Provide explainable predictions using Grad-CAM++.
Generate confidence-aware predictions.
Generate simple clinical recommendations.
Develop a user-friendly web application for glaucoma screening.


🚀 Proposed Workflow
Retinal Fundus Image
          │
          ▼
Image Quality Analysis
          │
          ▼
Adaptive Image Enhancement
(CLAHE / Gamma Correction /
Unsharp Masking /
Bilateral Filtering)
          │
          ▼
Image Normalization
          │
          ▼
EfficientNet-B3
          │
          ▼
Glaucoma Classification
(Normal / Glaucoma)
          │
          ▼
Grad-CAM++ Visualization
          │
          ▼
Confidence Score
          │
          ▼
Clinical Recommendation


📂 Datasets

The project uses publicly available glaucoma retinal image datasets:

ACRIMA Dataset
ORIGA Dataset
RIM-ONE DL Dataset
PAPILA Dataset

These datasets contain retinal fundus images collected from different hospitals and imaging devices, allowing the model to learn from diverse image conditions and improving its ability to generalize.

🧠 Deep Learning Model
Primary Model
EfficientNet-B3
Image Processing Techniques
CLAHE (Contrast Enhancement)
Gamma Correction (Brightness Adjustment)
Bilateral Filtering (Noise Removal)
Unsharp Masking (Image Sharpening)
Explainable AI
Grad-CAM++
🛠 Technologies Used
Python
TensorFlow
Keras
OpenCV
NumPy
Pandas
Scikit-learn
Matplotlib
Flask
HTML
CSS
JavaScript
Google Colab
GitHub


✨ Key Features
Adaptive Image Enhancement
Automatic Glaucoma Detection
Explainable AI using Grad-CAM++
Confidence Score Generation
Clinical Recommendation Generation
Multi-Dataset Evaluation
Web-Based Prediction System


📋 Expected Output

The system provides:

Glaucoma Prediction (Normal / Glaucoma)
Confidence Score
Grad-CAM++ Heatmap
Clinical Recommendation
Example

Prediction: Glaucoma Detected

Confidence: 97%

Recommendation: Consult an ophthalmologist for further clinical evaluation and additional eye examinations.

💡 Project Novelty

The proposed project introduces several innovative features compared to traditional glaucoma detection systems:

Adaptive Image Enhancement based on image quality instead of applying fixed preprocessing to every retinal image.
Automatic image quality analysis to choose the most suitable enhancement technique.
Explainable AI using Grad-CAM++ for transparent and trustworthy predictions.
Confidence-aware prediction to improve the reliability of the diagnosis.
Evaluation across multiple public glaucoma datasets (ACRIMA, ORIGA, RIM-ONE DL, and PAPILA) to demonstrate better model generalization.