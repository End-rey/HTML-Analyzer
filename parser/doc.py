from docx import Document


def parse(doc_path: str) -> str:
    """
    Parse a .doc/.docx file and extract clean text from it.

    Args:
        doc_path (str): Path to the .doc/.docx file

    Returns:
        str: Extracted text from the document
    """

    doc = Document(doc_path)

    full_text = []
    for paragraph in doc.paragraphs:
            if paragraph.text.strip():  
                full_text.append(paragraph.text)

    return '\n'.join(full_text)
