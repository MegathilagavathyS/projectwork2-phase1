
import cv2
import numpy as np

IMG_SIZE = (256, 256)
# ============================================================
# IMAGE QUALITY ANALYSIS
# ============================================================

def analyze_quality(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    contrast = np.std(gray)

    sharpness = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    return brightness,contrast,sharpness
# ============================================================
# CLAHE
# ============================================================

def apply_clahe(image):

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    l = clahe.apply(l)

    enhanced = cv2.merge((l, a, b))

    return cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
# ============================================================
# GAMMA CORRECTION
# ============================================================

def gamma_correction(image, gamma=1.5):

    inv_gamma = 1.0 / gamma

    table = np.array([
        ((i / 255.0) ** inv_gamma) * 255
        for i in np.arange(256)
    ]).astype("uint8")

    return cv2.LUT(image, table)
# ============================================================
# BILATERAL FILTER
# ============================================================

def bilateral_filter(image):

    return cv2.bilateralFilter(
        image,
        d=9,
        sigmaColor=75,
        sigmaSpace=75
    )
# ============================================================
# UNSHARP MASK
# ============================================================

def unsharp_mask(image):

    blur = cv2.GaussianBlur(image, (5,5), 0)

    sharpened = cv2.addWeighted(
        image,
        1.5,
        blur,
        -0.5,
        0
    )

    return sharpened
# ============================================================
# ADAPTIVE PREPROCESSING WITH QUALITY METRICS
# ============================================================

def adaptive_preprocessing(image):

    # Analyze image quality
    brightness, contrast, sharpness = analyze_quality(image)

    processed = image.copy()

    operations = []

    # Low Contrast
    if contrast < 40:
        processed = apply_clahe(processed)
        operations.append("CLAHE")

    # Dark Image
    if brightness < 80:
        processed = gamma_correction(processed)
        operations.append("Gamma Correction")

    # Blurry Image
    if sharpness < 80:
        processed = unsharp_mask(processed)
        operations.append("Unsharp Mask")

    # Always apply noise reduction
    processed = bilateral_filter(processed)
    operations.append("Bilateral Filter")

    # Resize
    processed = cv2.resize(processed, IMG_SIZE)

    if operations == ["Bilateral Filter"]:
        operations.append("No Adaptive Enhancement")

    return processed, operations, brightness, contrast, sharpness