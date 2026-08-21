import re
import tempfile
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import httpx

from app import crypto, models
from app.config import settings
from app.rag.transcription import transcribe_video

DRIVE_HOSTS = {"drive.google.com"}
# 200MB, not the 120MB browser-upload cap in main.py's MAX_REQUEST_BYTES --
# this is a server-to-server download, not a browser upload, so it isn't
# bounded by request-body limits, but still needs a ceiling on a 512MB-RAM
# instance.
MAX_DRIVE_VIDEO_BYTES = 200 * 1024 * 1024
_DOWNLOAD_CHUNK_BYTES = 1024 * 1024

# Drive's mimeType is authoritative -- more reliable than guessing an
# extension from the file's display name, which may have none or an
# unusual one. transcribe_video/Gemini's upload only needs a plausible
# video extension to infer the right mime type; unmapped video/* types
# fall back to .mp4, which is a safe generic container extension.
_MIME_TO_SUFFIX = {
    "video/mp4": ".mp4",
    "video/quicktime": ".mov",
    "video/x-matroska": ".mkv",
    "video/x-msvideo": ".avi",
    "video/webm": ".webm",
}

TOKEN_URL = "https://oauth2.googleapis.com/token"
DRIVE_API = "https://www.googleapis.com/drive/v3/files"


def is_drive_url(url: str) -> bool:
    return urlparse(url).hostname in DRIVE_HOSTS


def _extract_file_id(url: str) -> str | None:
    parsed = urlparse(url)
    match = re.search(r"/d/([\w-]+)", parsed.path)
    if match:
        return match.group(1)
    return parse_qs(parsed.query).get("id", [None])[0]


def _refresh_access_token(coach: models.Coach) -> str:
    if not coach.google_drive_refresh_token_encrypted:
        raise ValueError("Connect Google Drive in Settings first.")
    refresh_token = crypto.decrypt(coach.google_drive_refresh_token_encrypted)
    response = httpx.post(
        TOKEN_URL,
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": settings.google_client_id,
            "client_secret": settings.google_client_secret,
        },
        timeout=15,
    )
    if response.status_code != 200:
        raise ValueError("Your Google Drive connection has expired -- reconnect it in Settings.")
    return response.json()["access_token"]


def get_drive_video_info(url: str, coach: models.Coach) -> dict:
    """Fast path: validate a Drive URL and return its metadata, without
    downloading or transcribing anything. Raises ValueError -- safe to show
    a coach directly -- for anything that isn't a clean success: not
    connected, the file isn't a video, too large, or not accessible to this
    coach. Used both for instant feedback on bad input before committing to
    a background job, and as the first step of fetch_drive_video below.
    """
    file_id = _extract_file_id(url)
    if not file_id:
        raise ValueError("Couldn't find a file ID in that Google Drive URL.")

    access_token = _refresh_access_token(coach)
    headers = {"Authorization": f"Bearer {access_token}"}

    meta_response = httpx.get(
        f"{DRIVE_API}/{file_id}", params={"fields": "name,mimeType,size"}, headers=headers, timeout=15
    )
    if meta_response.status_code in (401, 403, 404):
        raise ValueError(
            "Couldn't access that Google Drive file -- make sure it's shared with your Google account "
            "(or with 'Anyone with the link'), and that your Drive connection in Settings is still active."
        )
    meta_response.raise_for_status()
    meta = meta_response.json()

    if not meta.get("mimeType", "").startswith("video/"):
        raise ValueError("That Google Drive file doesn't look like a video.")
    size = int(meta.get("size", 0))
    if size > MAX_DRIVE_VIDEO_BYTES:
        raise ValueError(
            f"That video is too large ({size // (1024 * 1024)}MB, max "
            f"{MAX_DRIVE_VIDEO_BYTES // (1024 * 1024)}MB) -- try a shorter clip or a lower-resolution export."
        )

    return {
        "file_id": file_id,
        "title": meta.get("name", "Google Drive video"),
        "mime_type": meta["mimeType"],
        "size": size,
        "access_token": access_token,
    }


def fetch_drive_video(url: str, coach: models.Coach) -> tuple[str, str]:
    """Download a Drive-hosted video and transcribe it -- entry point, wraps
    _fetch_drive_video so any network/API failure that isn't one of the
    explicit, specific ValueErrors below (a transient Drive 5xx, a request
    timeout, an unexpected response shape) still surfaces as a clean,
    readable message instead of propagating as a raw 500. transcribe_video's
    own Gemini-side failures are its own concern and pass through as-is.
    """
    try:
        return _fetch_drive_video(url, coach)
    except ValueError:
        raise
    except (httpx.HTTPError, KeyError) as e:
        raise ValueError(f"Something went wrong reaching Google Drive ({e}) -- try again in a moment.") from e


def _fetch_drive_video(url: str, coach: models.Coach) -> tuple[str, str]:
    # Re-validates even if the router already called get_drive_video_info
    # once -- this function is called from a background task started well
    # after that initial check, and a coach could disconnect Drive or the
    # access token could need refreshing in the meantime; the extra cheap
    # metadata call is worth not trusting stale state.
    info = get_drive_video_info(url, coach)
    file_id, title, size, access_token = info["file_id"], info["title"], info["size"], info["access_token"]
    headers = {"Authorization": f"Bearer {access_token}"}
    suffix = _MIME_TO_SUFFIX.get(info["mime_type"], ".mp4")

    downloaded_bytes = 0
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        with httpx.stream(
            "GET", f"{DRIVE_API}/{file_id}", params={"alt": "media"}, headers=headers, timeout=120
        ) as media_response:
            if media_response.status_code in (401, 403, 404):
                raise ValueError(
                    "Couldn't access that Google Drive file -- make sure it's shared with your Google "
                    "account (or with 'Anyone with the link'), and that your Drive connection in Settings "
                    "is still active."
                )
            media_response.raise_for_status()
            # A 200 with an HTML/text body (a "sign in" or permission
            # interstitial) instead of real binary video data is a real
            # failure mode Drive can return even with a valid-looking
            # token -- without this check it silently gets saved as the
            # resource's "transcript" (Gemini describing a webpage instead
            # of transcribing a video), which is worse than a clean error.
            content_type = media_response.headers.get("content-type", "")
            if content_type.startswith("text/"):
                raise ValueError(
                    "Google Drive returned a webpage instead of the video file -- this usually means your "
                    "Drive connection needs refreshing. Reconnect Google Drive in Settings and try again."
                )
            for chunk in media_response.iter_bytes(_DOWNLOAD_CHUNK_BYTES):
                downloaded_bytes += len(chunk)
                tmp.write(chunk)
    finally:
        tmp.close()

    # Cross-check against the size Drive's metadata reported -- a
    # significant mismatch (e.g. a few KB downloaded when metadata said
    # tens of MB) means what came back wasn't the real file, even if it
    # slipped past the content-type check above.
    if size and downloaded_bytes < size * 0.9:
        raise ValueError(
            "The downloaded file didn't match the video's expected size -- Google Drive may not have "
            "returned the real file. Reconnect Google Drive in Settings and try again."
        )

    text = transcribe_video(Path(tmp.name))
    return title, text
