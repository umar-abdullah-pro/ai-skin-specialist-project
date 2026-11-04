import os
import mimetypes
import time
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):

    gemini_api_key = os.environ.get("GEMINI_API_KEY")

    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file!")

    # Initialize Gemini client
    client = genai.Client(api_key=gemini_api_key)
    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    # Doctor's instructions
    prompt = (
        "You are an AI skin health assistant. "
        "Provide clear, reassuring and medically cautious information. "
        "Limit your entire response to two or three sentences maximum. "
        "If the patient has provided only an image and no video, "
        "politely ask them to provide a video showing the skin problem "
        "so that more visual details can be understood. "
        "Do not claim to provide a confirmed diagnosis. "
        "If the patient describes severe symptoms or an emergency, "
        "recommend appropriate medical attention. "
        "Do not use special characters, asterisks or markdown formatting "
        "because your response will be converted directly into audio.\n\n"
        f"Patient text: {patient_text}"
    )

    # Prepare Gemini input
    contents = [prompt]

    if video_filepath:
        # Upload video to Gemini
        video_file = client.files.upload(file=video_filepath)

        # Wait until video processing is complete
        while not video_file.state or video_file.state.name != "ACTIVE":
            if video_file.state and video_file.state.name == "FAILED":
                raise RuntimeError("Gemini could not process the video.")

            logging.info("Processing patient video...")
            time.sleep(5)
            video_file = client.files.get(name=video_file.name)

        contents.append(video_file)

    elif image_filepath:

        # Read image
        with open(image_filepath, "rb") as file:
            image_data = file.read()

        # Detect image type
        media_type, _ = mimetypes.guess_type(image_filepath)
        media_type = media_type or "image/jpeg"

        # Add image to Gemini input
        image_part = types.Part.from_bytes(data=image_data, mime_type=media_type)

        contents.append(image_part)

    # Generate doctor's response
    response = client.models.generate_content(model=model, contents=contents)

    doctors_response_in_text = response.text

    return doctors_response_in_text
