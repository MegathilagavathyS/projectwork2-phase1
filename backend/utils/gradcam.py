import tensorflow as tf
import numpy as np
import cv2


def find_last_conv_layer(model):
    # Search inside nested models
    for layer in reversed(model.layers):

        # If this layer is a nested model
        if isinstance(layer, tf.keras.Model):

            for sublayer in reversed(layer.layers):

                try:
                    shape = sublayer.output.shape

                    if len(shape) == 4:
                        print("Grad-CAM layer selected:", sublayer.name)
                        print("Layer output shape:", shape)
                        return sublayer

                except Exception:
                    continue

        else:

            try:
                shape = layer.output.shape

                if len(shape) == 4:
                    print("Grad-CAM layer selected:", layer.name)
                    print("Layer output shape:", shape)
                    return layer

            except Exception:
                continue

    raise ValueError("No suitable Grad-CAM layer found.")


def generate_gradcam(model, image):

    # Find convolutional layer
    last_conv_layer = find_last_conv_layer(model)

    # Get the EfficientNet base model
    base_model = None

    for layer in model.layers:
        if isinstance(layer, tf.keras.Model):
            base_model = layer
            break

    if base_model is None:
        raise ValueError("EfficientNet base model not found.")

    # Create Grad-CAM model from the base model
    grad_model = tf.keras.models.Model(
        inputs=base_model.input,
        outputs=[
            last_conv_layer.output,
            base_model.output
        ]
    )

    # Prepare image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb = cv2.resize(image_rgb, (300, 300))
    image_rgb = image_rgb.astype("float32")

    input_image = np.expand_dims(
        image_rgb,
        axis=0
    )

    # Forward pass
    with tf.GradientTape() as tape:

        conv_outputs, base_output = grad_model(
            input_image
        )

        # Recreate the final classification layers
        x = model.layers[-3](base_output)
        x = model.layers[-2](x)
        prediction = model.layers[-1](x)

        class_score = prediction[:, 0]

    # Gradients
    gradients = tape.gradient(
        class_score,
        conv_outputs
    )

    # Average gradients
    weights = tf.reduce_mean(
        gradients,
        axis=(1, 2)
    )

    # Weighted feature maps
    cam = tf.reduce_sum(
        conv_outputs * weights[:, tf.newaxis, tf.newaxis, :],
        axis=-1
    )

    # Remove batch dimension
    cam = cam[0]

    # Keep positive influence
    cam = tf.maximum(cam, 0)

    # Normalize
    cam = cam / (
        tf.reduce_max(cam)
        + tf.keras.backend.epsilon()
    )

    cam = cam.numpy()

    # Resize heatmap
    heatmap = cv2.resize(
        cam,
        (image.shape[1], image.shape[0])
    )

    heatmap = np.uint8(
        255 * heatmap
    )

    # Apply color map
    heatmap_color = cv2.applyColorMap(
        heatmap,
        cv2.COLORMAP_JET
    )

    # Overlay
    overlay = cv2.addWeighted(
        image,
        0.6,
        heatmap_color,
        0.4,
        0
    )

    return heatmap_color, overlay