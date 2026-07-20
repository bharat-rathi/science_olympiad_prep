from google import genai
from google.genai import types

from app.config import settings

_client: genai.Client | None = None


def _get_client() -> genai.Client:
    global _client
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a batch of strings with Gemini's text embedding model.

    This is the "E" in RAG: each chunk of text becomes a fixed-length vector
    such that semantically similar text ends up with similar vectors, which
    is what lets us later retrieve by meaning instead of by keyword.
    """
    if not texts:
        return []
    result = _get_client().models.embed_content(
        model=settings.gemini_embedding_model,
        contents=[types.Content(parts=[types.Part.from_text(text=t)]) for t in texts],
    )
    return [e.values for e in result.embeddings]


def embed_text(text: str) -> list[float]:
    return embed_texts([text])[0]
