from deepgram import DeepgramClient
import os
from dotenv import load_dotenv
from pathlib import Path
import platform
import subprocess

load_dotenv()

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

if not DEEPGRAM_API_KEY:
    raise ValueError("Deepgram API key not found!")

text = """
Hello, I am a virtual doctor.
I can help you with your skin concerns.
Please describe your symptoms or upload an image
of your skin condition for analysis.
"""

client = DeepgramClient(api_key=DEEPGRAM_API_KEY)

# Generate speech
audio_response = client.speak.v1.audio.generate(
    text=text,
    model="aura-2-thalia-en",
    encoding="linear16",
)

# Save audio
audio_path = Path(__file__).with_name("doctor_voice.wav")

with audio_path.open("wb") as file:
    for chunk in audio_response:
        file.write(chunk)

print("Audio generated successfully!")

# Play audio
if platform.system() == "Darwin":
    subprocess.run(["afplay", str(audio_path)])

elif platform.system() == "Windows":
    os.startfile(str(audio_path))

else:
    subprocess.run(["xdg-open", str(audio_path)])
