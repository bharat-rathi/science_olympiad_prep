from urllib.parse import parse_qs, urlparse

import requests
from youtube_transcript_api import YouTubeTranscriptApi

OEMBED_TIMEOUT_SECONDS = 5
YOUTUBE_HOSTS = {"www.youtube.com", "youtube.com", "m.youtube.com", "youtu.be"}


def is_youtube_url(url: str) -> bool:
    return urlparse(url).hostname in YOUTUBE_HOSTS


def _extract_video_id(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        return parsed.path.lstrip("/") or None
    if parsed.path == "/watch":
        return parse_qs(parsed.query).get("v", [None])[0]
    for prefix in ("/embed/", "/shorts/"):
        if parsed.path.startswith(prefix):
            return parsed.path[len(prefix):].split("/")[0] or None
    return None


def _fetch_title(url: str) -> str:
    try:
        response = requests.get(
            "https://www.youtube.com/oembed", params={"url": url, "format": "json"}, timeout=OEMBED_TIMEOUT_SECONDS
        )
        response.raise_for_status()
        return response.json().get("title", url)
    except requests.RequestException:
        return url


def fetch_youtube_transcript(url: str) -> tuple[str, str]:
    """Pull a YouTube video's official captions -- no LLM, no download.

    Returns (title, transcript_text). Raises ValueError with a message safe
    to show the coach directly if the URL isn't a recognizable YouTube link
    or the video has no captions available in any language.
    """
    video_id = _extract_video_id(url)
    if not video_id:
        raise ValueError("Couldn't find a video ID in that YouTube URL.")

    try:
        fetched = YouTubeTranscriptApi().fetch(video_id)
    except Exception as e:
        # The library's failure modes here (disabled captions, no captions in
        # any language, private/unavailable video, etc.) all mean the same
        # thing from a coach's point of view: nothing to ingest from this
        # video's captions, so uploading the file for transcription instead.
        raise ValueError(
            "This YouTube video doesn't have captions available to read -- try "
            "uploading it as a video file instead, or pasting a written summary."
        ) from e

    text = " ".join(snippet.text for snippet in fetched).strip()
    if not text:
        raise ValueError("This YouTube video's captions came back empty.")

    return _fetch_title(url), text
