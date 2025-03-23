from PyPDF2 import PdfReader

def parse(pdf_path: str) -> str:
    """
    Extract text from a PDF document.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """

    reader = PdfReader(pdf_path)
    text = ""
    
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    return text.strip()
