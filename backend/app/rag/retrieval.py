from app.config import settings
from app.llm.prompts import BATCH_RELEVANCE_SCHEMA, batch_relevance_judge_prompt
from app.llm.router import get_llm_handle
from app.rag.embeddings import embed_text
from app.rag.vectorstore import query_topic


def retrieve_relevant_chunks(topic_name: str, topic_description: str, topic_id: int, coach=None) -> list[dict]:
    """Retrieve then relevance-judge chunks for a topic.

    Two stages, deliberately kept separate:
      1. Embedding similarity retrieval (recall-oriented, cheap) pulls a
         candidate set from Chroma.
      2. A single batched LLM relevance-judge call (precision-oriented)
         scores every candidate at once against "does this substantively
         explain a concept a student needs," dropping anything below
         threshold -- one call for up to retrieval_top_k candidates, not one
         call per candidate, since this step runs on every "Generate concept
         explanations" click.

    Stage 2 is what keeps a merely-present video from dominating an
    explanation just because it exists -- it's scored by the same rubric as
    every other source, so a video with only rules/logistics content gets
    filtered out here rather than forced into the write-up.
    """
    query_embedding = embed_text(f"{topic_name}. {topic_description}")
    candidates = query_topic(topic_id, query_embedding, top_k=settings.retrieval_top_k)
    if not candidates:
        return []

    indexed = [{"index": i, "source_type": c["metadata"]["source_type"], "text": c["text"]} for i, c in enumerate(candidates)]
    system, user = batch_relevance_judge_prompt(topic_name, topic_description, indexed)
    result = get_llm_handle(coach).complete_json(
        system, user, BATCH_RELEVANCE_SCHEMA, max_tokens=1500, effort="low", label="relevance_judge_batch"
    )

    judgments_by_index = {j["index"]: j for j in result.get("judgments", []) if "index" in j}

    relevant = []
    for i, candidate in enumerate(candidates):
        judged = judgments_by_index.get(i)
        if not judged:
            continue
        score = judged.get("score", 0)
        if score >= settings.relevance_threshold:
            relevant.append({**candidate, "relevance_score": score, "relevance_reason": judged.get("reason", "")})
    return relevant


def retrieve_chunks_for_message(message: str, topic_id: int, top_k: int | None = None) -> list[dict]:
    """Embedding-similarity retrieval for one live chat turn.

    Unlike retrieve_relevant_chunks, this embeds the user's actual message
    (not a fixed topic name+description) and skips the relevance-judge LLM
    stage -- a chat loop needs one round-trip per turn, not two, and the QA
    prompt itself is expected to say so when nothing relevant comes back.
    """
    query_embedding = embed_text(message)
    return query_topic(topic_id, query_embedding, top_k=top_k or settings.retrieval_top_k)
