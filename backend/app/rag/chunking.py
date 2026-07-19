import tiktoken

_ENCODING = tiktoken.get_encoding("cl100k_base")

CHUNK_TOKENS = 500
OVERLAP_TOKENS = 75


def chunk_text(text: str, chunk_tokens: int = CHUNK_TOKENS, overlap_tokens: int = OVERLAP_TOKENS) -> list[str]:
    """Token-aware chunker: splits `text` into overlapping windows of ~chunk_tokens.

    Overlap keeps a concept that straddles a chunk boundary intact in at least
    one chunk, at the cost of embedding some tokens twice.
    """
    if not text.strip():
        return []

    tokens = _ENCODING.encode(text)
    if len(tokens) <= chunk_tokens:
        return [text]

    chunks = []
    start = 0
    step = chunk_tokens - overlap_tokens
    while start < len(tokens):
        window = tokens[start : start + chunk_tokens]
        chunks.append(_ENCODING.decode(window))
        if start + chunk_tokens >= len(tokens):
            break
        start += step
    return chunks
