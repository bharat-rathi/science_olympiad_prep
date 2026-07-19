from app.config import settings
from app.llm.client import complete_json
from app.llm.prompts import RELEVANCE_SCHEMA, relevance_judge_prompt
from app.rag.embeddings import embed_text
from app.rag.vectorstore import query_topic


def retrieve_relevant_chunks(topic_name: str, topic_description: str, topic_id: int) -> list[dict]:
    """Retrieve then relevance-judge chunks for a topic.

    Two stages, deliberately kept separate:
      1. Embedding similarity retrieval (recall-oriented, cheap) pulls a
         candidate set from Chroma.
      2. An LLM relevance-judge pass (precision-oriented) scores each
         candidate against "does this substantively explain a concept a
         student needs," dropping anything below threshold.

    Stage 2 is what keeps a merely-present video from dominating an
    explanation just because it exists -- it's scored by the same rubric as
    every other source, so a video with only rules/logistics content gets
    filtered out here rather than forced into the write-up.
    """
    query_embedding = embed_text(f"{topic_name}. {topic_description}")
    candidates = query_topic(topic_id, query_embedding, top_k=settings.retrieval_top_k)

    relevant = []
    for candidate in candidates:
        system, user = relevance_judge_prompt(
            topic_name, topic_description, candidate["metadata"]["source_type"], candidate["text"]
        )
        judged = complete_json(system, user, RELEVANCE_SCHEMA, max_tokens=200, effort="low")
        score = judged.get("score", 0)
        if score >= settings.relevance_threshold:
            relevant.append({**candidate, "relevance_score": score, "relevance_reason": judged.get("reason", "")})
    return relevant
