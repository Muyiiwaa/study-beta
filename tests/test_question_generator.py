import pytest
from core.question_generator import generate_questions

@pytest.fixture
def mock_openai(monkeypatch):
    class MockResponse:
        @staticmethod
        def create(engine, prompt, max_tokens, temperature):
            return {"choices": [{"text": "Q1: What is X?\nQ2: Explain Y."}]}
    
    monkeypatch.setattr("openai.Completion", MockResponse)

def test_generate_questions_valid_text(mock_openai):
    result = generate_questions("This is a test text.")
    assert len(result) == 2, "Two questions should be generated"
    assert result[0].startswith("Q1:"), "First question should start with Q1"

def test_generate_questions_empty_text(mock_openai):
    result = generate_questions("")
    assert len(result) == 0, "No questions should be generated for empty text"
