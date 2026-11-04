# Derma AI

A browser-based skin consultation interface for text, voice, image, and video
inputs. The interface provides informational guidance only and does not
diagnose medical conditions.

## Run locally

1. Install dependencies with `uv sync`.
2. Add `GEMINI_API_KEY` to `.env` for transcription and skin guidance.
3. Optionally add `DEEPGRAM_API_KEY` to `.env` for spoken responses.
4. Start the app with `uv run ai-skin-specialist` or `uv run main.py`.
5. Open <http://127.0.0.1:8000>.

The app binds to localhost by default. Audio, image, and video files are held
temporarily while a consultation is processed; consultation history is kept
only in the current browser page session. Submitted content is sent to the
configured AI providers for processing.