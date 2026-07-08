import os

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    "pdf",
    "docx",
    "txt"
}

# Maximum file size (20 MB)
MAX_FILE_SIZE = 20 * 1024 * 1024


def allowed_file(filename):
    """
    Check whether uploaded file extension is allowed.
    """

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in ALLOWED_EXTENSIONS


def validate_file(file):
    """
    Validate uploaded file.
    Returns:
        (True, "Valid") if file is valid
        (False, error_message) otherwise
    """

    if file.filename == "":
        return False, "No file selected."

    if not allowed_file(file.filename):
        return False, (
            "Unsupported file type. "
            "Only PDF, DOCX and TXT files are allowed."
        )

    # Check file size
    file.seek(0, os.SEEK_END)
    size = file.tell()
    file.seek(0)

    if size > MAX_FILE_SIZE:
        return False, "File size exceeds 20 MB."

    return True, "Valid"