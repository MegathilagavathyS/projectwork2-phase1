import cv2
from utils.preprocessing import adaptive_preprocessing
from utils.predict import predict_glaucoma

image = cv2.imread("test_image.jpg")

if image is None:
    print("Image not found!")
else:
    # Adaptive preprocessing
    processed, operations, brightness, contrast, sharpness = \
        adaptive_preprocessing(image)

    # Prediction
    label, confidence, probability = predict_glaucoma(processed)

    print("Prediction :", label)
    print("Confidence :", round(confidence, 2), "%")
    print("Probability:", round(probability, 4))

    print("\nPreprocessing Operations:")
    for op in operations:
        print("✓", op)