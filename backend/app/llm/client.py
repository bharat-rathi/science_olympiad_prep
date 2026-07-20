import json

from google import genai

from app.config import settings

_client: genai.Client | None = None

# Gemini's "thinking" tokens are spent invisibly before the visible output
# and count against max_output_tokens -- a low budget can truncate a response
# entirely if the model still tries to think first. Map our provider-neutral
# "effort" levels to Gemini's thinking_level so cheap classification-style
# calls (relevance judging, hints) skip thinking, while the two calls that
# actually benefit from deeper reasoning (concept explanations, quiz
# generation) keep it.
_THINKING_LEVEL = {"low": "minimal", "medium": "low", "high": "high"}


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


def _generation_config(max_tokens: int, effort: str) -> dict:
    return {"max_output_tokens": max_tokens, "thinking_level": _THINKING_LEVEL.get(effort, "low")}


def complete_text(system: str, user: str, max_tokens: int = 2000, effort: str = "medium") -> str:
    """Single place all generation calls go through -- swap providers here."""
    interaction = _get_client().interactions.create(
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
    )
    return interaction.output_text or ""


def complete_json(system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium") -> dict:
    """Same as complete_text, but constrains the response to the given JSON schema."""
    interaction = _get_client().interactions.create(
        model=settings.gemini_model,
        system_instruction=system,
        input=user,
        generation_config=_generation_config(max_tokens, effort),
        response_format={"type": "text", "mime_type": "application/json", "schema": schema},
    )
    return json.loads(interaction.output_text) if interaction.output_text else {}


def chat_turn(system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium") -> str:
    """Multi-turn conversational call, used by the tutor chat.

    Conversation history lives in our own TutorMessage table (see
    routers/tutor.py), so each turn we render that history into a single
    transcript rather than relying on the provider's own server-side session
    state -- keeps our DB the single source of truth for the conversation.
    """
    transcript = "\n\n".join(f"{'Student' if m['role'] == 'user' else 'Tutor'}: {m['content']}" for m in messages)
    interaction = _get_client().interactions.create(
        model=settings.gemini_model,
        system_instruction=system,
        input=transcript,
        generation_config=_generation_config(max_tokens, effort),
    )
    return interaction.output_text or ""
