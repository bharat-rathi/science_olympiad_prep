import json

import anthropic

from app.config import settings

_client: anthropic.Anthropic | None = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=settings.anthropic_api_key)
    return _client


def complete_text(system: str, user: str, max_tokens: int = 2000, effort: str = "medium") -> str:
    """Single place all generation calls go through — swap providers here."""
    response = _get_client().messages.create(
        model=settings.anthropic_model,
        max_tokens=max_tokens,
        system=system,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": user}],
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""


def complete_json(system: str, user: str, schema: dict, max_tokens: int = 2000, effort: str = "medium") -> dict:
    """Same as complete_text, but constrains the response to the given JSON schema."""
    response = _get_client().messages.create(
        model=settings.anthropic_model,
        max_tokens=max_tokens,
        system=system,
        output_config={"effort": effort, "format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": user}],
    )
    for block in response.content:
        if block.type == "text":
            return json.loads(block.text)
    return {}


def chat_turn(system: str, messages: list[dict], max_tokens: int = 1000, effort: str = "medium") -> str:
    """Multi-turn conversational call, used by the tutor chat."""
    response = _get_client().messages.create(
        model=settings.anthropic_model,
        max_tokens=max_tokens,
        system=system,
        output_config={"effort": effort},
        messages=messages,
    )
    for block in response.content:
        if block.type == "text":
            return block.text
    return ""
