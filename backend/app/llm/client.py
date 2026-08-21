import base64
import json
import logging
import random
import time

from google import genai

from app.config import settings

logger = logging.getLogger("llm_calls")

_client: genai.Client | None = None
# Per-coach personal Gemini keys build a fresh Client here rather than
# mutating the shared singleton above -- keeps the shared-default path
# (still the common case) byte-for-byte unchanged.

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


def _client_for(api_key: str | None) -> genai.Client:
    """The shared singleton for the default app key, or a fresh one-off
    client for a coach's personal Gemini key."""
    return _get_client() if api_key is None else genai.Client(api_key=api_key)


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


def _status_code(exc: Exception) -> int | None:
    # google-genai's exception hierarchy isn't stable across versions --
    # client.models.* raises errors.APIError (.code), while client.interactions.*
    # has been observed raising a private, differently-shaped error (e.g.
    # google.genai._interactions.RateLimitError, .status_code) after a minor
    # version bump. Duck-type instead of pinning to one class so retry
    # detection survives that drift; requirements.txt doesn't pin an exact
    # google-genai version, so this WILL happen again.
    for attr in ("code", "status_code"):
        value = getattr(exc, attr, None)
        if isinstance(value, int):
            return value
    return None


def _create_with_retry(fn=None, **kwargs):
    """Call a Gemini SDK method with backoff on rate-limit/server errors.

    Defaults to interactions.create (used by complete_text/complete_json/
    chat_turn/complete_text_grounded); generate_image passes
    models.generate_content instead, since image output isn't supported on
    the interactions.create path yet. Either way, this is the one retry
    layer everything bottlenecks through -- the one place that needs to
    change if we ever add a second provider to fail over to.
    """
    call = fn or _get_client().interactions.create
    last_error: Exception | None = None
    for attempt in range(_MAX_RETRIES + 1):
        try:
            if attempt:
                logger.info("llm_call retrying after rate-limit/server error, attempt=%d", attempt)
            return call(**kwargs)
        except Exception as e:
            code = _status_code(e)
            if code not in _RETRYABLE_CODES or attempt == _MAX_RETRIES:
                raise
            last_error = e
            delay = _BASE_DELAY_SECONDS * (2**attempt) + random.uniform(0, 1)
            time.sleep(delay)
    raise last_error  # pragma: no cover -- loop always returns or raises above


def complete_text(
    system: str, user: str, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    """Single place all generation calls go through -- swap providers here."""
    client = _client_for(api_key)
    interaction = _create_with_retry(
        fn=client.interactions.create,
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
    )
    text = interaction.output_text or ""
    _log_call(label or "complete_text", effort, len(system) + len(user), len(text))
    return text


def complete_json(
    system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> dict:
    """Same as complete_text, but constrains the response to the given JSON schema."""
    client = _client_for(api_key)
    interaction = _create_with_retry(
        fn=client.interactions.create,
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
        response_format={"type": "text", "mime_type": "application/json", "schema": schema},
    )
    text = interaction.output_text or ""
    _log_call(label or "complete_json", effort, len(system) + len(user), len(text))
    return json.loads(text) if text else {}


def complete_text_grounded(
    system: str, user: str, max_tokens: int = 3000, effort: str = "high", label: str = "", api_key: str | None = None
) -> str:
    """Same as complete_text, but lets the model search Google before answering.

    Used by rag/web_research.py (the research agent) when a coach types a
    bare keyword instead of pasting a link -- the model looks the topic up
    rather than answering purely from training data.

    Goes through models.generate_content (like generate_image) rather than
    interactions.create -- the latter's tools=[{"type": "google_search"}]
    wasn't reliably triggering real grounded search in production (results
    came back as bare restatements of the query), unlike the classic
    google_search Tool declaration used here.
    """
    client = _client_for(api_key)
    response = _create_with_retry(
        fn=client.models.generate_content,
        model=settings.gemini_model,
        contents=user,
        config={
            "system_instruction": system,
            "tools": [{"google_search": {}}],
            "max_output_tokens": max_tokens,
        },
    )
    text = response.text or ""
    _log_call(label or "complete_text_grounded", effort, len(system) + len(user), len(text))
    return text


def generate_image(prompt: str, label: str = "", api_key: str | None = None) -> bytes:
    """Generate one image from a text prompt via Gemini's native image model
    (settings.gemini_image_model, aka "nano banana").

    Returns raw image bytes (PNG). Raises ValueError -- safe to show a coach
    directly -- if the model responded without producing an image (e.g. it
    refused the prompt) or the API call itself failed (e.g. rate-limited
    past the retry budget).
    """
    client = _client_for(api_key)
    try:
        response = _create_with_retry(
            fn=client.models.generate_content,
            model=settings.gemini_image_model,
            contents=prompt,
            # image_config.image_size is documented in the SDK but verified
            # (see test in the PR) to have zero effect on this model's
            # output -- gemini-2.5-flash-image always returns 1024x1024
            # regardless of 1K/2K/4K, so it's deliberately not set here.
            # The actual fix for "images too small" was display-side (CSS),
            # not generation-side -- see flashcard-diagram/concept-image-preview.
            config={"response_modalities": ["TEXT", "IMAGE"]},
        )
    except Exception as e:
        raise ValueError(f"Image generation failed -- {e}") from e
    _log_call(label or "generate_image", "n/a", len(prompt), 0)
    candidates = response.candidates or []
    parts = candidates[0].content.parts if candidates and candidates[0].content else []
    for part in parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            return part.inline_data.data
    raise ValueError("Image generation didn't return an image -- try again or reword the concept.")


def describe_image(
    prompt: str, image_bytes: bytes, mime_type: str = "image/png", max_tokens: int = 800, label: str = "", api_key: str | None = None
) -> str:
    """Vision call -- used for PDF pages where plain text extraction comes
    back thin (scans, diagrams, charts). Goes through interactions.create
    (the default _create_with_retry path), same as complete_text/
    complete_json/chat_turn.
    """
    client = _client_for(api_key)
    interaction = _create_with_retry(
        fn=client.interactions.create,
        model=settings.gemini_model,
        input=[
            {"type": "text", "text": prompt},
            {"type": "image", "data": base64.b64encode(image_bytes).decode("ascii"), "mime_type": mime_type},
        ],
        generation_config=_generation_config(max_tokens, "low"),
    )
    text = interaction.output_text or ""
    _log_call(label or "describe_image", "low", len(prompt), len(text))
    return text


def chat_turn(
    system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium", label: str = "", api_key: str | None = None
) -> str:
    """Multi-turn conversational call, used by the tutor chat.

    Conversation history lives in our own TutorMessage table (see
    routers/tutor.py), so each turn we render that history into a single
    transcript rather than relying on the provider's own server-side session
    state -- keeps our DB the single source of truth for the conversation.
    """
    client = _client_for(api_key)
    transcript = "\n\n".join(f"{'Student' if m['role'] == 'user' else 'Tutor'}: {m['content']}" for m in messages)
    interaction = _create_with_retry(
        fn=client.interactions.create,
        model=settings.gemini_model,
        system_instruction=system,
        input=transcript,
        generation_config=_generation_config(max_tokens, effort),
    )
    text = interaction.output_text or ""
    _log_call(label or "chat_turn", effort, len(system) + len(transcript), len(text))
    return text
