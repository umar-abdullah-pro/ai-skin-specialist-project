import base64
import logging
import os
import tempfile
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from deepgram.core.api_error import ApiError as DeepgramApiError
from google.genai.errors import APIError as GeminiApiError
from starlette.concurrency import run_in_threadpool

from .brain_of_doctor import brain_of_the_doctor
from .voice_of_doctor import speak
from .voice_of_patient import transcribe_audio


logger = logging.getLogger(__name__)
web_dir = Path(__file__).with_name("web")
app = FastAPI(title="Derma AI Consultation")
app.mount("/assets", StaticFiles(directory=web_dir), name="assets")

MAX_FILE_SIZES = {
    "audio": 10 * 1024 * 1024,
    "image": 25 * 1024 * 1024,
    "video": 100 * 1024 * 1024,
}
ALLOWED_EXTENSIONS = {
    "audio": {".wav", ".mp3", ".m4a", ".webm", ".ogg", ".mp4", ".mpeg"},
    "image": {".jpg", ".jpeg", ".png", ".webp"},
    "video": {".mp4", ".mov", ".webm", ".m4v"},
}


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(web_dir / "index.html")


@app.get("/api/status")
async def status() -> dict[str, bool]:
    return {
        "analysis": bool(os.getenv("GEMINI_API_KEY")),
        "speech": bool(os.getenv("DEEPGRAM_API_KEY")),
    }


async def save_upload(
    upload: UploadFile | None, kind: str, directory: str
) -> str | None:
    if upload is None or not upload.filename:
        return None

    extension = Path(upload.filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS[kind]:
        raise HTTPException(status_code=415, detail=f"Unsupported {kind} file type.")

    content = await upload.read(MAX_FILE_SIZES[kind] + 1)
    if len(content) > MAX_FILE_SIZES[kind]:
        raise HTTPException(
            status_code=413,
            detail=f"{kind.capitalize()} files must be no larger than "
            f"{MAX_FILE_SIZES[kind] // (1024 * 1024)} MB.",
        )
    if not content:
        raise HTTPException(status_code=400, detail=f"The {kind} file is empty.")

    path = Path(directory) / f"{kind}{extension}"
    path.write_bytes(content)
    return str(path)


@app.post("/api/analyze")
async def analyze(
    concern: Annotated[str, Form()] = "",
    audio: Annotated[UploadFile | None, File()] = None,
    image: Annotated[UploadFile | None, File()] = None,
    video: Annotated[UploadFile | None, File()] = None,
) -> dict[str, str | None]:
    if not concern.strip() and not any((audio, image, video)):
        raise HTTPException(
            status_code=400,
            detail="Describe your concern or add an audio recording, image, or video.",
        )

    with tempfile.TemporaryDirectory(prefix="derma-ai-") as directory:
        audio_path = await save_upload(audio, "audio", directory)
        image_path = await save_upload(image, "image", directory)
        video_path = await save_upload(video, "video", directory)

        try:
            patient_text = concern.strip()
            if audio_path:
                transcript = await run_in_threadpool(transcribe_audio, audio_path)
                patient_text = " ".join(
                    part for part in (patient_text, transcript.strip()) if part
                )

            response_text = await run_in_threadpool(
                brain_of_the_doctor, patient_text, image_path, video_path
            )
            audio_base64 = None
            if os.getenv("DEEPGRAM_API_KEY"):
                audio_path_out = await run_in_threadpool(speak, response_text)
                try:
                    audio_base64 = base64.b64encode(
                        Path(audio_path_out).read_bytes()
                    ).decode("ascii")
                finally:
                    Path(audio_path_out).unlink(missing_ok=True)

        except ValueError as error:
            logger.warning("Consultation could not be completed: %s", error)
            raise HTTPException(status_code=503, detail=str(error)) from error
        except (RuntimeError, DeepgramApiError, GeminiApiError) as error:
            logger.warning("Consultation could not be completed: %s", error)
            raise HTTPException(status_code=502, detail=str(error)) from error

    return {
        "transcript": patient_text,
        "response": response_text,
        "audio": audio_base64,
        "audio_mime": "audio/mpeg" if audio_base64 else None,
    }


def main() -> None:
    import uvicorn

    uvicorn.run(
        "ai_skin_specialist.app:app", host="127.0.0.1", port=8000, reload=False
    )


if __name__ == "__main__":
    main()
