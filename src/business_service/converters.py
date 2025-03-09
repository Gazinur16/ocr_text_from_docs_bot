import io
from docx import Document

def convert_to_docx(full_text: str) -> io.BytesIO:
    """
    Конвертирует текст в документ DOCX.
    """
    buffer = io.BytesIO()
    doc = Document()

    for page in full_text.split("\n\n"):
        doc.add_paragraph(page)
    doc.save(buffer)
    buffer.seek(0)
    return buffer


def convert_to_txt(full_text: str) -> io.BytesIO:
    """
    Конвертирует текст в TXT файл.
    """
    buffer = io.BytesIO(full_text.encode("utf-8"))
    return buffer


def convert_to_md(full_text: str) -> io.BytesIO:
    """
    Конвертирует текст в Markdown файл.
    """
    buffer = io.BytesIO(full_text.encode("utf-8"))
    return buffer
