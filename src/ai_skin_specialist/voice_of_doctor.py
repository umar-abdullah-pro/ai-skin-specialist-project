import os
import tempfile
from pathlib import Path

from deepgram import DeepgramClient
from dotenv import load_dotenv


load_dotenv()


def speak(text: str) -> str:
    """Create a temporary spoken response and return its path."""
    api_key = os.getenv("DEEPGRAM_API_KEY")
    if not api_key:
        raise ValueError("DEEPGRAM_API_KEY is not configured.")

    client = DeepgramClient(api_key=api_key)
    audio_response = client.speak.v1.audio.generate(
        text=text,
        model="aura-2-thalia-en",
        encoding="mp3",
    )

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as audio_file:
        audio_path = Path(audio_file.name)
        for chunk in audio_response:
            audio_file.write(chunk)
    return str(audio_path)
