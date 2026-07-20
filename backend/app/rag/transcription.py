import tempfile
from pathlib import Path

from google import genai

from app.config import settings

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


def _transcribe_media(path: Path) -> str:
    """Upload a video/audio file to Gemini and ask for a transcript.

    Gemini accepts video and audio natively (multimodal), so there's no
    separate audio-extraction step -- the file goes up as-is and the model
    reads the audio track directly.
    """
    uploaded = _get_client().files.upload(file=str(path))
    interaction = _get_client().interactions.create(
        model=settings.gemini_model,
        input=[
            {"type": "text", "text": "Generate a transcript of the speech in this file."},
            {"type": "audio" if path.suffix.lower() in {".mp3", ".wav", ".m4a", ".flac"} else "video",
             "uri": uploaded.uri, "mime_type": uploaded.mime_type},
        ],
    )
    return interaction.output_text or ""


def transcribe_video(video_path: Path) -> str:
    return _transcribe_media(video_path)


def transcribe_audio(audio_path: Path) -> str:
    return _transcribe_media(audio_path)


def save_upload_to_temp(filename: str, data: bytes) -> Path:
    suffix = Path(filename).suffix or ".bin"
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp.write(data)
    tmp.close()
    return Path(tmp.name)
