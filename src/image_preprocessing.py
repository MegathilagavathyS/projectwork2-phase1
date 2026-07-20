import os
import cv2
import numpy as np

# ------------------------------
# Dataset Paths
# ------------------------------

INPUT_DATASET = "/content/drive/MyDrive/glucomadataset/dataset/datasetdivided"
OUTPUT_DATASET = "/content/drive/MyDrive/glucomadataset/dataset/EnhancedDataset"

# ------------------------------
# Enhancement Functions
# ------------------------------

def gamma_correction(image, gamma=1.8):

    invGamma = 1.0 / gamma

    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(256)]).astype("uint8")

    return cv2.LUT(image, table)


def apply_clahe(image):

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=3.0,
        tileGridSize=(8,8)
    )

    l = clahe.apply(l)

    lab = cv2.merge((l,a,b))

    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


def bilateral_filter(image):

    return cv2.bilateralFilter(
        image,
        9,
        75,
        75
    )


def unsharp_mask(image):

    blur = cv2.GaussianBlur(
        image,
        (9,9),
        10
    )

    sharp = cv2.addWeighted(
        image,
        2,
        blur,
        -1,
        0
    )

    return sharp


# ------------------------------
# Adaptive Preprocessing
# ------------------------------

def adaptive_preprocessing(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    contrast = gray.std()

    sharpness = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    noise = np.std(
        gray -
        cv2.GaussianBlur(gray,(5,5),0)
    )

    method = "None"

    if brightness < 70:

        image = gamma_correction(image)

        method = "Gamma Correction"

    elif contrast < 40:

        image = apply_clahe(image)

        method = "CLAHE"

    elif noise > 25:

        image = bilateral_filter(image)

        method = "Bilateral Filter"

    elif sharpness < 40:

        image = unsharp_mask(image)

        method = "Unsharp Masking"

    return image, method


# ------------------------------
# Process Complete Dataset
# ------------------------------

total_images = 0

for root, dirs, files in os.walk(INPUT_DATASET):

    for file in files:

        if file.lower().endswith((".jpg",".jpeg",".png")):

            input_path = os.path.join(root,file)

            relative_folder = os.path.relpath(
                root,
                INPUT_DATASET
            )

            output_folder = os.path.join(
                OUTPUT_DATASET,
                relative_folder
            )

            os.makedirs(
                output_folder,
                exist_ok=True
            )

            output_path = os.path.join(
                output_folder,
                file
            )

            image = cv2.imread(input_path)

            if image is None:
                continue

            enhanced_image, method = adaptive_preprocessing(image)

            cv2.imwrite(
                output_path,
                enhanced_image
            )

            total_images += 1

            print(f"{total_images} -> {file} | {method}")

print("\n======================================")
print("Adaptive Preprocessing Completed")
print("======================================")
print("Total Images Processed :", total_images)
print("Enhanced Dataset Saved At :")
print(OUTPUT_DATASET)