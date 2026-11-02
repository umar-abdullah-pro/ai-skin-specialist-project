from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OpenRouter API key not found!")

client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

folder = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(folder, "test-image.png")
video_path = os.path.join(folder, "test-video.mp4")

# Read and encode image
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

with open(video_path, "rb") as video_file:
    video_data = base64.b64encode(video_file.read()).decode("utf-8")

# Create data URLs
image_url = f"data:image/png;base64,{image_data}"
video_url = f"data:video/mp4;base64,{video_data}"

textMessage = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What can you help me with?"},
        ],
    }
]

imageMessage = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "you are a helpful skin analyst, please analyze this video and provide a detailed report on the skin condition of the patient.",
            },
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    }
]

videoMessage = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "you are a helpful skin analyst, please analyze this video and provide a detailed report on the skin condition of the patient.",
            },
            {"type": "video_url", "video_url": {"url": video_url}},
        ],
    }
]

response = client.chat.completions.create(
    model="openrouter/free", messages=imageMessage, max_tokens=1500
)

print(response.choices[0].message.content)
