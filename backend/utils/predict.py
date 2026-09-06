import os
import tensorflow as tf
import numpy as np
import cv2

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "efficientnetb3_glaucoma_experiment2.keras"
)

model = tf.keras.models.load_model(MODEL_PATH)


def predict_glaucoma(image):

    image = cv2.resize(image, (300, 300))

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    image = image.astype("float32")

    image = np.expand_dims(
        image,
        axis=0
    )

    probability = float(
        model.predict(
            image,
            verbose=0
        )[0][0]
    )

    if probability >= 0.5:

        label = "Glaucoma"
        confidence = probability * 100

    else:

        label = "Normal"
        confidence = (1 - probability) * 100

    return label, confidence, probability