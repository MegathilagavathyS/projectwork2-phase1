from flask import Flask, render_template, request
import os
import cv2
import uuid
import numpy as np
from utils.preprocessing import adaptive_preprocessing
from utils.predict import predict_glaucoma, model
from utils.gradcam import generate_gradcam


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

template_folder = os.path.join(
    BASE_DIR,
    "frontend",
    "templates"
)

static_folder = os.path.join(
    BASE_DIR,
    "frontend",
    "static"
)

app = Flask(
    __name__,
    template_folder=template_folder,
    static_folder=static_folder
)


# Result folder
RESULT_FOLDER = os.path.join(
    static_folder,
    "results"
)

os.makedirs(
    RESULT_FOLDER,
    exist_ok=True
)


# ---------------- HOME ----------------

@app.route("/")
def home():

    return render_template(
        "home.html"
    )


# ---------------- ABOUT GLAUCOMA ----------------

@app.route("/glaucoma")
def glaucoma():

    return render_template(
        "glaucoma.html"
    )


# ---------------- UPLOAD ----------------

@app.route("/upload")
def upload():

    return render_template(
        "upload.html"
    )


# ---------------- PREDICTION ----------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    # Check image
    if "image" not in request.files:

        return "No image uploaded"

    file = request.files["image"]

    if file.filename == "":

        return "No image selected"


    # Generate unique filename
    image_id = str(uuid.uuid4())

    original_filename = (
        image_id + "_original.jpg"
    )

    overlay_filename = (
        image_id + "_gradcam.jpg"
    )

    heatmap_filename = (
        image_id + "_heatmap.jpg"
    )


    # Read uploaded image
    file_bytes = file.read()

    image = cv2.imdecode(
    np.frombuffer(
        file_bytes,
        dtype=np.uint8
    ),
    cv2.IMREAD_COLOR
)


    if image is None:

        return "Invalid image"


    # Save original image
    original_path = os.path.join(
        RESULT_FOLDER,
        original_filename
    )

    cv2.imwrite(
        original_path,
        image
    )


    # ---------------- ADAPTIVE PREPROCESSING ----------------

    processed, operations, brightness, contrast, sharpness = \
        adaptive_preprocessing(image)


    # ---------------- PREDICTION ----------------

    label, confidence, probability = \
        predict_glaucoma(processed)


    # ---------------- GRAD-CAM ----------------

    heatmap, overlay = generate_gradcam(
        model,
        processed
    )


    # Save Grad-CAM
    overlay_path = os.path.join(
        RESULT_FOLDER,
        overlay_filename
    )

    heatmap_path = os.path.join(
        RESULT_FOLDER,
        heatmap_filename
    )


    cv2.imwrite(
        overlay_path,
        overlay
    )

    cv2.imwrite(
        heatmap_path,
        heatmap
    )


    # ---------------- RISK LEVEL ----------------

    if label == "Glaucoma":

        risk_level = "Requires Attention"

    else:

        risk_level = "Low Risk"


    # ---------------- RECOMMENDATION ----------------

    if label == "Glaucoma":

        recommendation = (
            "The model detected features associated "
            "with glaucoma. Please consult an "
            "ophthalmologist for further evaluation."
        )

    else:

        recommendation = (
            "The model did not detect features "
            "associated with glaucoma. Regular eye "
            "screening is recommended."
        )


    return render_template(
        "prediction.html",

        label=label,

        confidence=round(
            confidence,
            2
        ),

        probability=round(
            probability * 100,
            2
        ),

        risk_level=risk_level,

        recommendation=recommendation,

        original_image=(
            "results/" +
            original_filename
        ),

        gradcam_image=(
            "results/" +
            overlay_filename
        ),

        heatmap_image=(
            "results/" +
            heatmap_filename
        ),

        operations=operations,

        brightness=round(
            brightness,
            2
        ),

        contrast=round(
            contrast,
            2
        ),

        sharpness=round(
            sharpness,
            2
        )
    )


# ---------------- ABOUT PROJECT ----------------

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# ---------------- CONTACT ----------------

@app.route("/contact")
def contact():

    return render_template(
        "contact.html"
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )