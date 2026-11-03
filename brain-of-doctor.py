from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time
import mimetypes

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)

folder = os.path.dirname(os.path.abspath(__file__))

image_path = os.path.join(folder, "test-image.png")
video_path = os.path.join(folder, "test-video.mp4")


# Read image
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

image_mime = mimetypes.guess_type(image_path)[0]


# Upload video
video_file = client.files.upload(file=video_path)

while video_file.state.name == "PROCESSING":
    print("Processing video...")
    time.sleep(3)
    video_file = client.files.get(name=video_file.name)

if video_file.state.name != "ACTIVE":
    raise RuntimeError("Video processing failed!")


# TEXT MESSAGE
textMessage = [
    {"role": "user", "parts": [{"text": "Hello, what can you help me with?"}]}
]


# IMAGE MESSAGE
imageMessage = [
    {
        "role": "user",
        "parts": [
            {"inline_data": {"mime_type": image_mime, "data": image_data}},
            {"text": """
                You are a helpful skin analyst.

                Analyze this facial image and provide a detailed report
                describing visible acne, redness, inflammation,
                pigmentation, and skin texture.

                Provide general skincare recommendations.
                Do not make a definitive medical diagnosis.
                """},
        ],
    }
]


# VIDEO MESSAGE
videoMessage = [
    {
        "role": "user",
        "parts": [
            {
                "file_data": {
                    "mime_type": video_file.mime_type,
                    "file_uri": video_file.uri,
                }
            },
            {"text": """
                You are a helpful skin analyst.

                Analyze this video and provide a detailed report
                describing visible acne, redness, inflammation,
                pigmentation, and affected facial areas.

                Provide general skincare recommendations.
                Do not make a definitive medical diagnosis.
                """},
        ],
    }
]


# SELECT MESSAGE HERE
response = client.models.generate_content(
    model="gemini-3.8-flash", contents=videoMessage
)

print(response.text)
