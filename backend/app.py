from flask import Flask, render_template
import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define frontend paths
template_folder = os.path.join(BASE_DIR, "frontend", "templates")
static_folder = os.path.join(BASE_DIR, "frontend", "static")

# Create Flask app
app = Flask(
    __name__,
    template_folder=template_folder,
    static_folder=static_folder
)

# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("home.html")

# ---------------- ABOUT GLAUCOMA ----------------

@app.route("/glaucoma")
def glaucoma():
    return render_template("glaucoma.html")

# ---------------- UPLOAD ----------------

@app.route("/upload")
def upload():
    return render_template("upload.html")

# ---------------- PREDICTION ----------------

@app.route("/predict", methods=["POST"])
def predict():

    return render_template("prediction.html")

# ---------------- ABOUT PROJECT ----------------

@app.route("/about")
def about():
    return render_template("about.html")

# ---------------- CONTACT ----------------

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)