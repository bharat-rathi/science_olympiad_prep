from openai import OpenAI

from app.config import settings

_client: OpenAI | None = None


def _get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=settings.openai_api_key)
    return _client


def embed_texts(texts: list[str]) -> list[list[float]]:
    """Embed a batch of strings with OpenAI's text-embedding-3-small.

    This is the "E" in RAG: each chunk of text becomes a fixed-length vector
    such that semantically similar text ends up with similar vectors, which
    is what lets us later retrieve by meaning instead of by keyword.
    """
    if not texts:
        return []
    response = _get_client().embeddings.create(model=settings.openai_embedding_model, input=texts)
    return [item.embedding for item in response.data]


def embed_text(text: str) -> list[float]:
    return embed_texts([text])[0]
