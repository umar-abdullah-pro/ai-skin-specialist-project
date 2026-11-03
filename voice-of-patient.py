import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def record_audio(file_path, timeout=20, phrase_time_limit=10):
    """Record audio from the microphone and save it as a WAV file."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        logging.info("Recording audio...")
        audio_data = recognizer.listen(
            source, timeout=timeout, phrase_time_limit=phrase_time_limit
        )

        logging.info("Audio recording complete.")

        wav_data = audio_data.get_wav_data()

        audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
        audio_segment.export(file_path, format="wav")

        logging.info(f"Audio saved to {file_path}")


audio_filepath = "patient_audio.wav"
record_audio(audio_filepath)

# Gemini Speech-to-Text Transcription

gemini_api_key = os.environ.get("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

client = genai.Client(api_key=gemini_api_key)
audio_file = client.files.upload(file=audio_filepath)

transcription = client.interactions.create(
    model="gemini-3.5-transcribe",
    input=[
        {
            "type": "audio",
            "uri": audio_file.uri,
            "mime_type": audio_file.mime_type
        }
    ]
)

print("\nPatient's Transcription:")
print(transcription.output_text)

logging.info("Patient audio transcription completed successfully.")
