from pypdf import PdfReader
from docx import Document


def read_pdf(file_path):

    text = ""

    pdf = PdfReader(file_path)

    for page in pdf.pages:
        text += page.extract_text() + "\n"

    return text


def read_docx(file_path):

    doc = Document(file_path)

    text = "\n".join(
        paragraph.text
        for paragraph in doc.paragraphs
    )

    return text


def read_txt(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


def extract_text(
    file_path,
    file_type
):

    if file_type == "pdf":
        return read_pdf(file_path)

    if file_type == "docx":
        return read_docx(file_path)

    if file_type == "txt":
        return read_txt(file_path)

    return "Unsupported file type"