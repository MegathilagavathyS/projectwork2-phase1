import tensorflow as tf
import numpy as np
import cv2

MODEL_PATH = r"D:\Documents\Research_Project\projectwork2-phase1\Model_Training\efficientnetb3_glaucoma_experiment2.keras"

model = tf.keras.models.load_model(MODEL_PATH)

def predict_glaucoma(image):
    # Resize to model input size
    image = cv2.resize(image, (300, 300))

    # OpenCV BGR → RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to float32
    image = image.astype("float32")

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Prediction
    probability = float(model.predict(image, verbose=0)[0][0])

    if probability >= 0.5:
        label = "Glaucoma"
        confidence = probability * 100
    else:
        label = "Normal"
        confidence = (1 - probability) * 100

    return label, confidence, probability