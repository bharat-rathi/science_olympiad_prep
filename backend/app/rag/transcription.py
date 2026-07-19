import shutil
import subprocess
import tempfile
from pathlib import Path

from openai import OpenAI

from app.config import settings


class FfmpegNotFoundError(RuntimeError):
    pass


def _extract_audio(video_path: Path) -> Path:
    if shutil.which("ffmpeg") is None:
        raise FfmpegNotFoundError(
            "ffmpeg is not installed or not on PATH. Install it to enable video ingestion "
            "(https://ffmpeg.org/download.html)."
        )
    audio_path = video_path.with_suffix(".mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-i", str(video_path), "-vn", "-acodec", "libmp3lame", "-ar", "16000", "-ac", "1", str(audio_path)],
        check=True,
        capture_output=True,
    )
    return audio_path


def transcribe_video(video_path: Path) -> str:
    """Extract audio from a video file and transcribe it with OpenAI Whisper.

    Kept as a single explicit step (extract -> transcribe) rather than hidden
    behind a generic "ingest" call, so it's obvious where cost/time is spent.
    """
    audio_path = _extract_audio(video_path)
    return transcribe_audio(audio_path)


def transcribe_audio(audio_path: Path) -> str:
    client = OpenAI(api_key=settings.openai_api_key)
    with open(audio_path, "rb") as f:
        transcript = client.audio.transcriptions.create(model=settings.openai_transcribe_model, file=f)
    return transcript.text


def save_upload_to_temp(filename: str, data: bytes) -> Path:
    suffix = Path(filename).suffix or ".bin"
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    tmp.write(data)
    tmp.close()
    return Path(tmp.name)
