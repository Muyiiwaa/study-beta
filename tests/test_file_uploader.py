import pytest
from services.file_uploader import extract_pdf_text

def test_extract_pdf_text_valid_file(tmp_path):
    # Create a temporary PDF file with text
    pdf_path = tmp_path / "test.pdf"
    with open(pdf_path, "wb") as f:
        from PyPDF2 import PdfWriter
        writer = PdfWriter()
        writer.add_blank_page(width=200, height=200)
        writer.write(f)
    
    with open(pdf_path, "rb") as pdf_file:
        result = extract_pdf_text(pdf_file)
        assert isinstance(result, str), "Result should be a string"

def test_extract_pdf_text_invalid_file():
    invalid_file = "not_a_pdf.txt"
    with pytest.raises(Exception):
        extract_pdf_text(invalid_file)
