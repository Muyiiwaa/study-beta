from core.text_processor import clean_text, split_into_chunks

def test_clean_text():
    raw_text = "This   is   a  \n test! 🚀"
    cleaned_text = clean_text(raw_text)
    assert cleaned_text == "This is a test!", "Text should be cleaned of extra spaces and emojis"

def test_split_into_chunks():
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit." * 10
    chunks = split_into_chunks(text, chunk_size=100)
    assert len(chunks) > 1, "Text should be split into multiple chunks"
    assert all(len(chunk) <= 100 for chunk in chunks), "Each chunk should not exceed the specified chunk size"
