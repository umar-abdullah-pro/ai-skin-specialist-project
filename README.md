# Derma AI

Derma AI is a browser-based skin consultation interface. Describe a concern in
text, add an audio recording, photo, or video, and receive brief, cautious
health information. It does not diagnose skin conditions or replace a
qualified healthcare professional.

## Features

- Text-based skin concern descriptions
- Audio transcription and optional spoken responses
- Photo and video uploads for additional context
- Consultation history kept only in the current browser page session

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/)
- A Google Gemini API key
- A Deepgram API key is optional and enables spoken responses

## Run locally

1. Install the project dependencies:

   ```powershell
   uv sync
   ```

2. Create a `.env` file in the project root and add your Gemini API key:

   ```dotenv
   GEMINI_API_KEY=your_gemini_api_key
   ```

   To enable spoken responses, also add:

   ```dotenv
   DEEPGRAM_API_KEY=your_deepgram_api_key
   ```

3. Start the app:

   ```powershell
   uv run ai-skin-specialist
   ```

   Alternatively, run `uv run main.py`.

4. Open <http://127.0.0.1:8000>.

The app binds to localhost by default.

## Configuration

| Variable | Required | Description |
| --- | --- | --- |
| `GEMINI_API_KEY` | Yes | Used for audio transcription and skin guidance. |
| `DEEPGRAM_API_KEY` | No | Enables spoken versions of responses. |
| `GEMINI_MODEL` | No | Gemini model for skin guidance; defaults to `gemini-3.8-flash`. |
| `GEMINI_TRANSCRIPTION_MODEL` | No | Gemini model for transcription; defaults to the value of `GEMINI_MODEL`. |

If `GEMINI_TRANSCRIPTION_MODEL` is not set, transcription uses `GEMINI_MODEL`;
if neither is set, the app defaults to `gemini-3.8-flash`.

## Upload limits

- Audio: 10 MB
- Images: 25 MB
- Video: 100 MB

## Privacy and safety

Uploaded audio, images, and video are held in temporary storage while a
consultation is processed and then removed. The app does not persist
consultation history on the server; history lasts only for the current browser
page session. Submitted text and media are sent to Google Gemini for
transcription or analysis, and responses are sent to Deepgram for speech
generation when `DEEPGRAM_API_KEY` is configured.

Derma AI provides informational guidance only. Do not use it for emergencies
or as a substitute for professional medical advice, diagnosis, or treatment.
