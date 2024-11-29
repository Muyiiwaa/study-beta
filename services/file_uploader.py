import PyPDF2
from typing import Optional

def extract_pdf_text(pdf_file) -> Optional[str]:
    """
    Extract text content from an uploaded PDF file.
    
    Args:
        pdf_file: Uploaded PDF file object.
    
    Returns:
        Extracted text as a single string or None if extraction fails.
    """
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text.strip() if text else None
    except Exception as e:
        print(f"Error extracting PDF text: {e}")
        return None
