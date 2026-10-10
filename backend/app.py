from flask import Flask, render_template, request
from werkzeug.exceptions import RequestEntityTooLarge
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
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024 + 64 * 1024


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


@app.errorhandler(RequestEntityTooLarge)
def request_too_large(error):

    return render_template(
        "upload.html",
        error="The image must be 10 MB or smaller."
    ), 413


# ---------------- PREDICTION ----------------

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    if "image" not in request.files:
        return render_template(
            "upload.html",
            error="Choose an image to continue."
        ), 400

    file = request.files["image"]

    if file.filename == "":
        return render_template(
            "upload.html",
            error="Choose an image to continue."
        ), 400

    extension = os.path.splitext(file.filename)[1].lower()
    if extension not in {".jpg", ".jpeg", ".png"}:
        return render_template(
            "upload.html",
            error="Use a JPG, JPEG, or PNG image."
        ), 400


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


    file_bytes = file.read()

    if not file_bytes:
        return render_template(
            "upload.html",
            error="The selected file is empty."
        ), 400

    try:
        image = cv2.imdecode(
            np.frombuffer(file_bytes, dtype=np.uint8),
            cv2.IMREAD_COLOR
        )
    except cv2.error:
        image = None

    if image is None:
        return render_template(
            "upload.html",
            error="The file could not be read as an image. Try another JPG, JPEG, or PNG."
        ), 400

    height, width = image.shape[:2]
    if width * height > 40_000_000:
        return render_template(
            "upload.html",
            error="The image dimensions are too large. Use an image with no more than 40 megapixels."
        ), 400


    original_path = os.path.join(
        RESULT_FOLDER,
        original_filename
    )

    if not cv2.imwrite(original_path, image):
        app.logger.error("Could not save uploaded image to %s", original_path)
        return render_template(
            "upload.html",
            error="The server could not save the uploaded image. Please try again."
        ), 500


    processed, operations, brightness, contrast, sharpness = \
        adaptive_preprocessing(image)

    label, _confidence, probability = \
        predict_glaucoma(processed)

    heatmap, overlay = generate_gradcam(
        model,
        processed
    )

    overlay_path = os.path.join(
        RESULT_FOLDER,
        overlay_filename
    )

    heatmap_path = os.path.join(
        RESULT_FOLDER,
        heatmap_filename
    )


    if not cv2.imwrite(overlay_path, overlay):
        app.logger.error("Could not save Grad-CAM overlay to %s", overlay_path)
        return render_template(
            "upload.html",
            error="The server could not save the analysis visualization. Please try again."
        ), 500

    if not cv2.imwrite(heatmap_path, heatmap):
        app.logger.error("Could not save Grad-CAM heatmap to %s", heatmap_path)
        return render_template(
            "upload.html",
            error="The server could not save the analysis visualization. Please try again."
        ), 500

    if label == "Glaucoma":
        risk_level = "Review with an eye-care professional"
    else:
        risk_level = "No model flag; routine screening still matters"

    if label == "Glaucoma":
        recommendation = (
            "The model flagged this image for follow-up. Arrange an evaluation "
            "with an eye-care professional; this result is not a diagnosis."
        )
    else:
        recommendation = (
            "The model did not flag this image. This cannot rule out glaucoma; "
            "continue routine eye examinations and seek care for any concerns."
        )

    return render_template(
        "prediction.html",

        label=label,

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