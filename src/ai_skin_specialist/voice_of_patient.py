import mimetypes
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


def transcribe_audio(audio_filepath: str) -> str:
    """Transcribe a patient audio file using Gemini."""
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    audio_path = Path(audio_filepath)
    mime_type, _ = mimetypes.guess_type(audio_path.name)
    mime_type = {
        ".webm": "audio/webm",
        ".m4a": "audio/mp4",
        ".mp4": "audio/mp4",
        ".mpeg": "audio/mpeg",
    }.get(audio_path.suffix.lower(), mime_type)
    if not mime_type or not mime_type.startswith("audio/"):
        raise ValueError(f"Unsupported audio file type: {audio_path.suffix or 'unknown'}.")

    audio_data = audio_path.read_bytes()
    if not audio_data:
        raise ValueError("The audio recording is empty.")

    client = genai.Client(api_key=gemini_api_key)
    transcription = client.models.generate_content(
        model=os.getenv(
            "GEMINI_TRANSCRIPTION_MODEL",
            os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
        ),
        contents=[
            (
                "Transcribe the audible speech in this recording verbatim. "
                "Preserve the spoken language and return only the transcript. "
                "If no speech is audible, return [NO_SPEECH]."
            ),
            types.Part.from_bytes(data=audio_data, mime_type=mime_type),
        ],
    )
    patient_text = (transcription.text or "").strip()
    if not patient_text or patient_text == "[NO_SPEECH]":
        raise RuntimeError(
            "No speech could be transcribed from this recording. "
            "Try a recording with clearer speech or describe your concern in text."
        )
    return patient_text
