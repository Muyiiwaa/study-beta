from youtube_transcript_api import YouTubeTranscriptApi
from typing import Optional

def extract_youtube_text(video_url: str) -> Optional[str]:
    """
    Extract text content (transcript) from a YouTube video.
    
    Args:
        video_url: URL of the YouTube video.
    
    Returns:
        Combined transcript text as a single string or None if extraction fails.
    """
    try:
        # Extract video ID from the URL
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Error extracting YouTube transcript: {e}")
        return None
