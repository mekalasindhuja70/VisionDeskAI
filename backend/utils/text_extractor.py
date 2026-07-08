import os
import fitz  # PyMuPDF
from docx import Document


def extract_text(file_path):
    """
    Extract text from TXT, PDF, or DOCX files.
    """

    extension = os.path.splitext(file_path)[1].lower()

    # TXT File
    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    # PDF File
    elif extension == ".pdf":
        text = ""
        pdf = fitz.open(file_path)

        for page in pdf:
            text += page.get_text()

        pdf.close()
        return text

    # DOCX File
    elif extension == ".docx":
        doc = Document(file_path)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        return "Unsupported file format."