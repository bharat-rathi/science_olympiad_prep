from dataclasses import dataclass
from typing import Callable


@dataclass
class LLMHandle:
    """A bound set of the 6 generation calls, backed by one provider+key.

    Every adapter (gemini_client, claude_adapter, openai_adapter) exposes
    functions with these same signatures, so router.py can wire them up
    without call sites caring which provider is underneath.
    """

    provider: str
    complete_text: Callable[..., str]
    complete_json: Callable[..., dict]
    complete_text_grounded: Callable[..., str]
    generate_image: Callable[..., bytes]
    describe_image: Callable[..., str]
    chat_turn: Callable[..., str]
