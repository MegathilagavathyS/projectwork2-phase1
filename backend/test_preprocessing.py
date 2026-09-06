import cv2
from utils.preprocessing import adaptive_preprocessing

image = cv2.imread("test_image.jpg")

if image is None:
    print("Image not found!")
else:
    processed, operations, brightness, contrast, sharpness = \
        adaptive_preprocessing(image)

    print("Brightness :", round(brightness, 2))
    print("Contrast   :", round(contrast, 2))
    print("Sharpness  :", round(sharpness, 2))

    print("\nOperations Applied:")
    for op in operations:
        print("✓", op)

    print("\nProcessed Image Shape:", processed.shape)

    cv2.imwrite("processed_test.jpg", processed)

    print("\nAdaptive preprocessing successful!")