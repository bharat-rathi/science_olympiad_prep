import json
import logging
import random
import time

from google import genai
from google.genai import errors

from app.config import settings

logger = logging.getLogger("llm_calls")

_client: genai.Client | None = None

# Gemini's "thinking" tokens are spent invisibly before the visible output
# and count against max_output_tokens -- a low budget can truncate a response
# entirely if the model still tries to think first. Map our provider-neutral
# "effort" levels to Gemini's thinking_level so cheap classification-style
# calls (relevance judging, hints) skip thinking, while the two calls that
# actually benefit from deeper reasoning (concept explanations, quiz
# generation) keep it.
_THINKING_LEVEL = {"low": "minimal", "medium": "low", "high": "high"}

# Retryable: 429 (free-tier rate limit -- resets on its own, not a sign the
# request is wrong) and 5xx (transient server-side issues). Not retryable:
# other 4xx (400 bad request, 403 auth, etc.) -- those need a code/config
# fix, not a delay.
_RETRYABLE_CODES = {429, 500, 502, 503, 504}
_MAX_RETRIES = 3
_BASE_DELAY_SECONDS = 2.0


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


def _generation_config(max_tokens: int, effort: str) -> dict:
    return {"max_output_tokens": max_tokens, "thinking_level": _THINKING_LEVEL.get(effort, "low")}


def _log_call(label: str, effort: str, input_chars: int, output_chars: int, attempt: int = 0) -> None:
    # Visibility into LLM call volume/cost without a full usage-metrics
    # pipeline -- watch Render's logs for how often each label fires, and
    # for retries, how often Gemini's free tier is actually rate-limiting us.
    retry_note = f" retry={attempt}" if attempt else ""
    logger.info(
        "llm_call label=%s effort=%s input_chars=%d output_chars=%d%s", label, effort, input_chars, output_chars, retry_note
    )


def _create_with_retry(**kwargs):
    """Call Gemini's interactions.create with backoff on rate-limit/server errors.

    A single retry layer shared by complete_text/complete_json/chat_turn --
    all of them bottleneck through this function, so this is the one place
    that needs to change if we ever add a second provider to fail over to.
    """
    last_error: errors.APIError | None = None
    for attempt in range(_MAX_RETRIES + 1):
        try:
            if attempt:
                logger.info("llm_call retrying after rate-limit/server error, attempt=%d", attempt)
            return _get_client().interactions.create(**kwargs)
        except errors.APIError as e:
            if e.code not in _RETRYABLE_CODES or attempt == _MAX_RETRIES:
                raise
            last_error = e
            delay = _BASE_DELAY_SECONDS * (2**attempt) + random.uniform(0, 1)
            time.sleep(delay)
    raise last_error  # pragma: no cover -- loop always returns or raises above


def complete_text(system: str, user: str, max_tokens: int = 2000, effort: str = "medium", label: str = "") -> str:
    """Single place all generation calls go through -- swap providers here."""
    interaction = _create_with_retry(
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
    )
    text = interaction.output_text or ""
    _log_call(label or "complete_text", effort, len(system) + len(user), len(text))
    return text


def complete_json(
    system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium", label: str = ""
) -> dict:
    """Same as complete_text, but constrains the response to the given JSON schema."""
    interaction = _create_with_retry(
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
        response_format={"type": "text", "mime_type": "application/json", "schema": schema},
    )
    text = interaction.output_text or ""
    _log_call(label or "complete_json", effort, len(system) + len(user), len(text))
    return json.loads(text) if text else {}


def chat_turn(system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium", label: str = "") -> str:
    """Multi-turn conversational call, used by the tutor chat.

    Conversation history lives in our own TutorMessage table (see
    routers/tutor.py), so each turn we render that history into a single
    transcript rather than relying on the provider's own server-side session
    state -- keeps our DB the single source of truth for the conversation.
    """
    transcript = "\n\n".join(f"{'Student' if m['role'] == 'user' else 'Tutor'}: {m['content']}" for m in messages)
    interaction = _create_with_retry(
        model=settings.gemini_model,
        system_instruction=system,
        input=transcript,
        generation_config=_generation_config(max_tokens, effort),
    )
    text = interaction.output_text or ""
    _log_call(label or "chat_turn", effort, len(system) + len(transcript), len(text))
    return text
