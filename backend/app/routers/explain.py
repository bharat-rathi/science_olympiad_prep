from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db
from app.llm.client import complete_json
from app.llm.prompts import CONCEPT_LIST_SCHEMA, explanation_prompt
from app.rag.retrieval import retrieve_relevant_chunks

router = APIRouter(prefix="/api/topics", tags=["explain"])


@router.post("/{topic_id}/generate-explanations", response_model=list[schemas.ConceptTermOut])
def generate_explanations(
    topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    relevant_chunks = retrieve_relevant_chunks(topic.name, topic.description, topic_id)

    labeled_snippets = [{"source_type": c["metadata"]["source_type"], "text": c["text"]} for c in relevant_chunks]
    system, user = explanation_prompt(topic.name, topic.description, labeled_snippets)
    result = complete_json(
        system, user, CONCEPT_LIST_SCHEMA, max_tokens=4000, effort="high", label="generate_explanations"
    )

    grounding_resource_ids = sorted({c["metadata"]["resource_id"] for c in relevant_chunks})
    video_resource_ids = {
        c["metadata"]["resource_id"] for c in relevant_chunks if c["metadata"]["source_type"] == "video"
    }

    # Clear out unapproved concepts from a previous "Generate" click before
    # inserting the fresh batch, so re-clicking replaces the draft glossary
    # instead of piling up duplicates -- concepts the coach already approved
    # are left untouched.
    db.query(models.ConceptTerm).filter(
        models.ConceptTerm.topic_id == topic_id, models.ConceptTerm.approved.is_(False)
    ).delete()

    created = []
    for concept in result.get("concepts", []):
        grounded = concept["source"] == "team_resource"
        term = models.ConceptTerm(
            topic_id=topic_id,
            term=concept["term"],
            explanation_md=concept["explanation_md"],
            source_resource_ids=grounding_resource_ids if grounded else [],
            video_relevant=grounded and bool(video_resource_ids),
            approved=False,
        )
        db.add(term)
        created.append(term)

    db.commit()
    for term in created:
        db.refresh(term)
    return created
