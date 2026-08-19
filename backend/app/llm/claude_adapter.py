import base64
import functools
import json
import random
import time

import anthropic

from app.config import settings
from app.llm.handle import LLMHandle

# Retryable: 429 (rate limit) and 5xx (transient). Not retryable: other 4xx --
# those need a code/config fix (e.g. a bad key), not a delay. Separate from
# llm/client.py's Gemini retry logic since Anthropic's exception shape
# (APIStatusError.status_code) is different from google-genai's.
_RETRYABLE_CODES = {429, 500, 502, 503, 504}
_MAX_RETRIES = 3
_BASE_DELAY_SECONDS = 2.0


def _status_code(exc: Exception) -> int | None:
    return getattr(exc, "status_code", None)


def _with_retry(fn):
    last_error: Exception | None = None
    for attempt in range(_MAX_RETRIES + 1):
        try:
            return fn()
        except Exception as e:
            code = _status_code(e)
            if code not in _RETRYABLE_CODES or attempt == _MAX_RETRIES:
                raise
            last_error = e
            time.sleep(_BASE_DELAY_SECONDS * (2**attempt) + random.uniform(0, 1))
    raise last_error  # pragma: no cover -- loop always returns or raises above


def _text_of(response) -> str:
    return "".join(b.text for b in response.content if b.type == "text")


def complete_text(
    system: str, user: str, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = _with_retry(
        lambda: client.messages.create(
            model=settings.claude_model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": effort},
            messages=[{"role": "user", "content": user}],
        )
    )
    return _text_of(response)


def complete_json(
    system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> dict:
    """Uses Claude's native structured-output format -- no tool-forcing needed."""
    client = anthropic.Anthropic(api_key=api_key)
    response = _with_retry(
        lambda: client.messages.create(
            model=settings.claude_model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
            messages=[{"role": "user", "content": user}],
        )
    )
    text = _text_of(response)
    return json.loads(text) if text else {}


def complete_text_grounded(
    system: str, user: str, max_tokens: int = 3000, effort: str = "high", label: str = "", api_key: str | None = None
) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    response = _with_retry(
        lambda: client.messages.create(
            model=settings.claude_model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": effort},
            tools=[{"type": "web_search_20260209", "name": "web_search"}],
            messages=[{"role": "user", "content": user}],
        )
    )
    return _text_of(response)


def describe_image(
    prompt: str, image_bytes: bytes, mime_type: str = "image/png", max_tokens: int = 800, label: str = "", api_key: str | None = None
) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    b64 = base64.b64encode(image_bytes).decode("ascii")
    response = _with_retry(
        lambda: client.messages.create(
            model=settings.claude_model,
            max_tokens=max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "image", "source": {"type": "base64", "media_type": mime_type, "data": b64}},
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
        )
    )
    return _text_of(response)


def chat_turn(
    system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    client = anthropic.Anthropic(api_key=api_key)
    transcript = "\n\n".join(f"{'Student' if m['role'] == 'user' else 'Tutor'}: {m['content']}" for m in messages)
    response = _with_retry(
        lambda: client.messages.create(
            model=settings.claude_model,
            max_tokens=max_tokens,
            system=system,
            thinking={"type": "adaptive"},
            output_config={"effort": effort},
            messages=[{"role": "user", "content": transcript}],
        )
    )
    return _text_of(response)


def build(api_key: str, fallback: LLMHandle) -> LLMHandle:
    """Claude has no image-generation API -- generate_image delegates to the
    shared Gemini fallback handle so a Claude-configured coach's flashcard
    images still work, just not on their own key/budget.
    """
    bind = functools.partial
    return LLMHandle(
        provider="claude",
        complete_text=bind(complete_text, api_key=api_key),
        complete_json=bind(complete_json, api_key=api_key),
        complete_text_grounded=bind(complete_text_grounded, api_key=api_key),
        generate_image=fallback.generate_image,
        describe_image=bind(describe_image, api_key=api_key),
        chat_turn=bind(chat_turn, api_key=api_key),
    )
