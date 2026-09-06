import cv2
import tensorflow as tf

from utils.preprocessing import adaptive_preprocessing
from utils.gradcam import generate_gradcam


MODEL_PATH = r"D:\Documents\Research_Project\projectwork2-phase1\Model_Training\efficientnetb3_glaucoma_final.keras"

# Load model
model = tf.keras.models.load_model(MODEL_PATH)

# Load image
image = cv2.imread("test_image.jpg")

if image is None:
    print("Image not found!")

else:

    # Adaptive preprocessing
    processed, operations, brightness, contrast, sharpness = \
        adaptive_preprocessing(image)

    print("Preprocessing Operations:")

    for op in operations:
        print("✓", op)

    print("\nGenerating Grad-CAM...")

    # Generate heatmap
    heatmap, overlay = generate_gradcam(
        model,
        processed
    )

    # Save results
    cv2.imwrite(
        "gradcam_heatmap.jpg",
        heatmap
    )

    cv2.imwrite(
        "gradcam_overlay.jpg",
        overlay
    )

    print("\nGrad-CAM successful!")

    print("Saved:")
    print("✓ gradcam_heatmap.jpg")
    print("✓ gradcam_overlay.jpg")