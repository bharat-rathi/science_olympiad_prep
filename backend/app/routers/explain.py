import base64

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db
from app.llm.router import get_llm_handle
from app.llm.prompts import (
    CONCEPT_LIST_SCHEMA,
    REFINE_CONCEPT_SCHEMA,
    STORY_SCHEMA,
    explanation_prompt,
    image_prompt,
    refine_concept_prompt,
    story_prompt,
)
from app.rag.retrieval import retrieve_relevant_chunks

router = APIRouter(prefix="/api/topics", tags=["explain"])


@router.post("/{topic_id}/generate-explanations", response_model=list[schemas.ConceptTermOut])
def generate_explanations(
    topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    llm = get_llm_handle(coach)
    relevant_chunks = retrieve_relevant_chunks(topic.name, topic.description, topic_id, coach)

    labeled_snippets = [{"source_type": c["metadata"]["source_type"], "text": c["text"]} for c in relevant_chunks]
    system, user = explanation_prompt(topic.name, topic.description, labeled_snippets)
    # max_tokens=8000 (not 4000): this generates a whole LIST of concepts in
    # one JSON call, and Gemini's invisible "thinking" tokens at effort="high"
    # count against this same budget -- 4000 was occasionally getting
    # truncated mid-string on topics with several concepts (same class of
    # issue already fixed for refine_concept/generate_story, just needed a
    # bigger ceiling here since this call's real output is larger).
    result = llm.complete_json(
        system, user, CONCEPT_LIST_SCHEMA, max_tokens=8000, effort="high", label="generate_explanations"
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
            analogy=concept.get("analogy", ""),
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


@router.post("/{topic_id}/concepts/{concept_id}/refine", response_model=schemas.ConceptTermOut)
def refine_concept(
    topic_id: int,
    concept_id: int,
    payload: schemas.ConceptFeedbackRequest,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Revise one concept's explanation/analogy per coach feedback.

    Single cheap LLM call -- no retrieval re-run, since the concept is
    already grounded and revising wording doesn't need new source material.
    """
    concept = db.get(models.ConceptTerm, concept_id)
    if not concept or concept.topic_id != topic_id:
        raise HTTPException(404, "Concept not found")

    topic = db.get(models.Topic, topic_id)
    system, user = refine_concept_prompt(topic.name, concept.term, concept.explanation_md, concept.analogy, payload.feedback)
    # effort="medium" (not "high"): this is a wording revision, not synthesis
    # from source material, so it doesn't need deep reasoning -- cheaper, and
    # avoids Gemini's invisible "thinking" tokens eating the whole max_tokens
    # budget before any visible output is written (see llm/client.py).
    result = get_llm_handle(coach).complete_json(
        system, user, REFINE_CONCEPT_SCHEMA, max_tokens=2000, effort="medium", label="refine_concept"
    )

    concept.explanation_md = result["explanation_md"]
    concept.analogy = result["analogy"]
    db.commit()
    db.refresh(concept)
    return concept


@router.post("/{topic_id}/concepts/{concept_id}/generate-image", response_model=schemas.ConceptTermOut)
def generate_concept_image(
    topic_id: int,
    concept_id: int,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Review agent's visual step: a kid-friendly illustration for one flashcard.

    Single image-gen call, no retrieval -- the concept is already reviewed
    and approved-or-not; this just adds a picture to it.
    """
    concept = db.get(models.ConceptTerm, concept_id)
    if not concept or concept.topic_id != topic_id:
        raise HTTPException(404, "Concept not found")

    topic = db.get(models.Topic, topic_id)
    prompt = image_prompt(topic.name, concept.term, concept.explanation_md, concept.analogy)
    try:
        image_bytes = get_llm_handle(coach).generate_image(prompt, label="generate_concept_image")
    except ValueError as e:
        raise HTTPException(422, str(e))

    concept.image_data_url = "data:image/png;base64," + base64.b64encode(image_bytes).decode("ascii")
    db.commit()
    db.refresh(concept)
    return concept


@router.post("/{topic_id}/generate-story", response_model=schemas.TopicOut)
def generate_story(topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    approved = db.query(models.ConceptTerm).filter(
        models.ConceptTerm.topic_id == topic_id, models.ConceptTerm.approved.is_(True)
    ).all()
    if not approved:
        raise HTTPException(400, "No approved concepts yet -- approve at least one before generating a story")

    system, user = story_prompt(topic.name, [{"term": c.term, "explanation_md": c.explanation_md} for c in approved])
    # Generous max_tokens headroom -- Gemini's invisible "thinking" tokens at
    # effort="high" count against this budget before any visible output is
    # written, and a 300-600 word story plus thinking can add up fast.
    result = get_llm_handle(coach).complete_json(system, user, STORY_SCHEMA, max_tokens=4000, effort="high", label="generate_story")

    topic.story_md = result["story_md"]
    db.commit()
    db.refresh(topic)
    return schemas.TopicOut.from_model(topic)
