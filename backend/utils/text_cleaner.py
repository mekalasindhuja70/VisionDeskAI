import re

def clean_text(text):
    """
    Clean extracted text by removing
    unnecessary spaces and blank lines.
    """

    # Remove multiple spaces
    text = re.sub(r' +', ' ', text)

    # Remove tabs
    text = text.replace("\t", " ")

    # Remove multiple blank lines
    text = re.sub(r'\n+', '\n', text)

    return text.strip()