import functools

from app import crypto, models
from app.llm import client as gemini_client
from app.llm.handle import LLMHandle

_shared_default: LLMHandle | None = None


def _gemini_handle(api_key: str | None) -> LLMHandle:
    bind = functools.partial
    return LLMHandle(
        provider="gemini",
        complete_text=bind(gemini_client.complete_text, api_key=api_key),
        complete_json=bind(gemini_client.complete_json, api_key=api_key),
        complete_text_grounded=bind(gemini_client.complete_text_grounded, api_key=api_key),
        generate_image=bind(gemini_client.generate_image, api_key=api_key),
        describe_image=bind(gemini_client.describe_image, api_key=api_key),
        chat_turn=bind(gemini_client.chat_turn, api_key=api_key),
    )


def _shared_default_handle() -> LLMHandle:
    global _shared_default
    if _shared_default is None:
        _shared_default = _gemini_handle(api_key=None)
    return _shared_default


def get_llm_handle(coach: "models.Coach | None", raw_api_key: str | None = None) -> LLMHandle:
    """Resolve which provider+key backs the next call.

    Falls back to the shared app default (today's Gemini behavior,
    unchanged) whenever `coach` is None (public/student-facing endpoints,
    e.g. tutor.py) or hasn't set a personal provider+key. `raw_api_key` lets
    the ai-settings save endpoint validate a submitted key with one live
    call before it's ever persisted or decrypted.
    """
    if raw_api_key is not None:
        provider = coach.llm_provider if coach else None
        api_key = raw_api_key
    elif coach is not None and coach.llm_provider and coach.llm_api_key_encrypted:
        provider = coach.llm_provider
        api_key = crypto.decrypt(coach.llm_api_key_encrypted)
    else:
        return _shared_default_handle()

    if provider == "gemini":
        return _gemini_handle(api_key=api_key)
    if provider == "claude":
        from app.llm import claude_adapter

        return claude_adapter.build(api_key, fallback=_shared_default_handle())
    if provider == "openai":
        from app.llm import openai_adapter

        return openai_adapter.build(api_key, fallback=_shared_default_handle())
    return _shared_default_handle()
