import uuid

import chromadb

from app.config import settings

_client = None
_collection = None

COLLECTION_NAME = "resource_chunks"


def _get_collection():
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path=settings.chroma_dir)
        # embedding_function=None: we embed explicitly via rag/embeddings.py and
        # pass vectors in ourselves, rather than letting Chroma call an
        # embedding model implicitly — keeps the RAG pipeline's steps visible.
        _collection = _client.get_or_create_collection(name=COLLECTION_NAME)
    return _collection


def add_chunks(
    topic_id: int,
    resource_id: int,
    source_type: str,
    chunks: list[str],
    embeddings: list[list[float]],
) -> None:
    if not chunks:
        return
    collection = _get_collection()
    ids = [str(uuid.uuid4()) for _ in chunks]
    metadatas = [
        {"topic_id": topic_id, "resource_id": resource_id, "source_type": source_type, "chunk_index": i}
        for i in range(len(chunks))
    ]
    collection.add(ids=ids, embeddings=embeddings, documents=chunks, metadatas=metadatas)


def query_topic(topic_id: int, query_embedding: list[float], top_k: int) -> list[dict]:
    """Return up to top_k chunks for a topic, ranked by embedding similarity."""
    collection = _get_collection()
    if collection.count() == 0:
        return []
    result = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"topic_id": topic_id},
    )
    if not result["ids"] or not result["ids"][0]:
        return []
    out = []
    for i in range(len(result["ids"][0])):
        out.append(
            {
                "text": result["documents"][0][i],
                "metadata": result["metadatas"][0][i],
                "distance": result["distances"][0][i],
            }
        )
    return out


def delete_resource(resource_id: int) -> None:
    collection = _get_collection()
    collection.delete(where={"resource_id": resource_id})
