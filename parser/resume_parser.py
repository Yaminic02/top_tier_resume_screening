import fitz
import docx
import re
import tempfile

def extract_text(uploaded_file):
    text = ""

    suffix = uploaded_file.name.split(".")[-1].lower()

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix="."+suffix) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    if suffix == "pdf":
        doc = fitz.open(temp_path)
        text = " ".join(page.get_text() for page in doc)

    elif suffix == "docx":
        doc = docx.Document(temp_path)
        text = " ".join(p.text for p in doc.paragraphs)

    # CLEAN TEXT (CRITICAL)
    text = re.sub(r"[\u2022•\-]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.lower()
