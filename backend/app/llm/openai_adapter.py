import base64
import functools
import json
import random
import time

import openai

from app.config import settings
from app.llm.handle import LLMHandle

# Same retryable/non-retryable split as claude_adapter.py and llm/client.py --
# separate from both since OpenAI's exception shape differs from Anthropic's
# and google-genai's.
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


# Our "low"/"medium"/"high" effort vocabulary maps directly onto
# reasoning_effort for OpenAI's reasoning-capable models; harmless to pass
# on non-reasoning models too (ignored there).
def _reasoning_effort(effort: str) -> str:
    return {"low": "low", "medium": "medium", "high": "high"}.get(effort, "medium")


def complete_text(
    system: str, user: str, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    client = openai.OpenAI(api_key=api_key)
    response = _with_retry(
        lambda: client.chat.completions.create(
            model=settings.openai_model,
            max_completion_tokens=max_tokens,
            reasoning_effort=_reasoning_effort(effort),
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        )
    )
    return response.choices[0].message.content or ""


def complete_json(
    system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> dict:
    client = openai.OpenAI(api_key=api_key)
    response = _with_retry(
        lambda: client.chat.completions.create(
            model=settings.openai_model,
            max_completion_tokens=max_tokens,
            reasoning_effort=_reasoning_effort(effort),
            response_format={"type": "json_schema", "json_schema": {"name": "response", "schema": schema, "strict": True}},
            messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        )
    )
    text = response.choices[0].message.content or ""
    return json.loads(text) if text else {}


def complete_text_grounded(
    system: str, user: str, max_tokens: int = 3000, effort: str = "high", label: str = "", api_key: str | None = None
) -> str:
    """Uses the Responses API (not Chat Completions) -- that's where OpenAI's
    hosted web_search tool lives."""
    client = openai.OpenAI(api_key=api_key)
    response = _with_retry(
        lambda: client.responses.create(
            model=settings.openai_model,
            instructions=system,
            input=user,
            max_output_tokens=max_tokens,
            tools=[{"type": "web_search"}],
        )
    )
    return response.output_text or ""


def generate_image(prompt: str, label: str = "", api_key: str | None = None) -> bytes:
    client = openai.OpenAI(api_key=api_key)
    try:
        response = _with_retry(
            lambda: client.images.generate(
                model=settings.openai_image_model,
                prompt=prompt,
                n=1,
                response_format="b64_json",
            )
        )
    except Exception as e:
        raise ValueError(f"Image generation failed -- {e}") from e
    data = response.data or []
    if data and data[0].b64_json:
        return base64.b64decode(data[0].b64_json)
    raise ValueError("Image generation didn't return an image -- try again or reword the concept.")


def describe_image(
    prompt: str, image_bytes: bytes, mime_type: str = "image/png", max_tokens: int = 800, label: str = "", api_key: str | None = None
) -> str:
    client = openai.OpenAI(api_key=api_key)
    b64 = base64.b64encode(image_bytes).decode("ascii")
    response = _with_retry(
        lambda: client.chat.completions.create(
            model=settings.openai_model,
            max_completion_tokens=max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{b64}"}},
                    ],
                }
            ],
        )
    )
    return response.choices[0].message.content or ""


def chat_turn(
    system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    client = openai.OpenAI(api_key=api_key)
    transcript = "\n\n".join(f"{'Student' if m['role'] == 'user' else 'Tutor'}: {m['content']}" for m in messages)
    response = _with_retry(
        lambda: client.chat.completions.create(
            model=settings.openai_model,
            max_completion_tokens=max_tokens,
            reasoning_effort=_reasoning_effort(effort),
            messages=[{"role": "system", "content": system}, {"role": "user", "content": transcript}],
        )
    )
    return response.choices[0].message.content or ""


def build(api_key: str, fallback: LLMHandle) -> LLMHandle:
    bind = functools.partial
    return LLMHandle(
        provider="openai",
        complete_text=bind(complete_text, api_key=api_key),
        complete_json=bind(complete_json, api_key=api_key),
        complete_text_grounded=bind(complete_text_grounded, api_key=api_key),
        generate_image=bind(generate_image, api_key=api_key),
        describe_image=bind(describe_image, api_key=api_key),
        chat_turn=bind(chat_turn, api_key=api_key),
    )
