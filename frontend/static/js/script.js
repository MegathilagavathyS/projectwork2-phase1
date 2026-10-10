const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const previewPanel = document.getElementById("previewPanel");
const fileName = document.getElementById("fileName");
const fileError = document.getElementById("fileError");
const dropzone = document.getElementById("dropzone");
const uploadForm = document.getElementById("uploadForm");
const submitButton = document.getElementById("submitButton");

if (imageInput && preview && previewPanel) {
    const maxFileSize = 10 * 1024 * 1024;
    let previewUrl = null;

    const clearPreview = () => {
        if (previewUrl) {
            URL.revokeObjectURL(previewUrl);
            previewUrl = null;
        }
        preview.removeAttribute("src");
        previewPanel.hidden = true;
        fileName.textContent = "";
    };

    const showError = (message) => {
        fileError.textContent = message;
        imageInput.classList.add("is-invalid");
        clearPreview();
    };

    const clearError = () => {
        fileError.textContent = "";
        imageInput.classList.remove("is-invalid");
    };

    const showFile = (file) => {
        clearError();
        if (!file) {
            clearPreview();
            return false;
        }

        const validType = ["image/jpeg", "image/png"].includes(file.type);
        const validExtension = /\.(jpe?g|png)$/i.test(file.name);
        if (!validType || !validExtension) {
            showError("Choose a JPG, JPEG, or PNG image.");
            return false;
        }
        if (file.size > maxFileSize) {
            showError("The image must be 10 MB or smaller.");
            return false;
        }

        if (previewUrl) {
            URL.revokeObjectURL(previewUrl);
        }
        previewUrl = URL.createObjectURL(file);
        preview.src = previewUrl;
        fileName.textContent = file.name;
        previewPanel.hidden = false;
        return true;
    };

    imageInput.addEventListener("change", () => {
        showFile(imageInput.files[0]);
    });

    document.getElementById("removeImage").addEventListener("click", () => {
        imageInput.value = "";
        clearError();
        clearPreview();
        imageInput.focus();
    });

    if (dropzone) {
        ["dragenter", "dragover"].forEach((eventName) => {
            dropzone.addEventListener(eventName, (event) => {
                event.preventDefault();
                dropzone.classList.add("is-dragging");
            });
        });

        ["dragleave", "drop"].forEach((eventName) => {
            dropzone.addEventListener(eventName, (event) => {
                event.preventDefault();
                dropzone.classList.remove("is-dragging");
            });
        });

        dropzone.addEventListener("drop", (event) => {
            const [file] = event.dataTransfer.files;
            if (!file) {
                return;
            }
            const transfer = new DataTransfer();
            transfer.items.add(file);
            imageInput.files = transfer.files;
            showFile(file);
        });
    }

    uploadForm.addEventListener("submit", (event) => {
        if (!showFile(imageInput.files[0])) {
            event.preventDefault();
            imageInput.focus();
            return;
        }
        submitButton.disabled = true;
        submitButton.querySelector(".button-label").hidden = true;
        submitButton.querySelector(".button-loading").hidden = false;
    });
}
