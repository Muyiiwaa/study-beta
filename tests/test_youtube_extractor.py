import pytest
from services.youtube_extractor import extract_youtube_text

def test_extract_youtube_text_valid_url(monkeypatch):
    # Mock the YouTubeTranscriptApi response
    def mock_get_transcript(video_id):
        return [{"text": "This is a test transcript."}]
    
    monkeypatch.setattr("youtube_transcript_api.YouTubeTranscriptApi.get_transcript", mock_get_transcript)
    
    result = extract_youtube_text("https://www.youtube.com/watch?v=testvideo")
    assert result == "This is a test transcript.", "Transcript text should match the mocked response"

def test_extract_youtube_text_invalid_url():
    result = extract_youtube_text("https://www.invalid-url.com")
    assert result is None, "Result should be None for invalid URLs"
