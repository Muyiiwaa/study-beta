import re
from typing import List

def clean_text(text: str) -> str:
    """
    Clean text by removing unnecessary characters and whitespace.
    
    Args:
        text: Raw input text.
    
    Returns:
        Cleaned text.
    """
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    return text.strip()

def split_into_chunks(text: str, chunk_size: int = 1000) -> List[str]:
    """
    Split text into smaller chunks of a specified size.
    
    Args:
        text: Input text.
        chunk_size: Maximum size of each chunk.
    
    Returns:
        List of text chunks.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
