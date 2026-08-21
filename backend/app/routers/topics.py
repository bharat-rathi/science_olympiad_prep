from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db

router = APIRouter(prefix="/api/topics", tags=["topics"])


@router.get("", response_model=list[schemas.TopicOut])
def list_topics(db: Session = Depends(get_db)):
    topics = db.query(models.Topic).order_by(models.Topic.id).all()
    return [schemas.TopicOut.from_model(t) for t in topics]


@router.post("", response_model=schemas.TopicOut)
def create_topic(
    payload: schemas.TopicCreate, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    topic = models.Topic(**payload.model_dump(), created_by_coach_id=coach.id)
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return schemas.TopicOut.from_model(topic)


@router.get("/{topic_id}", response_model=schemas.TopicOut)
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    return schemas.TopicOut.from_model(topic)


@router.patch("/{topic_id}/story", response_model=schemas.TopicOut)
def update_story(
    topic_id: int,
    payload: schemas.TopicStoryUpdate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Manual edit of an already-generated story -- no LLM call."""
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    topic.story_md = payload.story_md
    db.commit()
    db.refresh(topic)
    return schemas.TopicOut.from_model(topic)


@router.post("/{topic_id}/publish-content", response_model=schemas.TopicOut)
def publish_content(topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    topic.content_published = True
    db.commit()
    db.refresh(topic)
    return schemas.TopicOut.from_model(topic)


@router.post("/{topic_id}/unpublish-content", response_model=schemas.TopicOut)
def unpublish_content(topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    topic.content_published = False
    db.commit()
    db.refresh(topic)
    return schemas.TopicOut.from_model(topic)


@router.get("/{topic_id}/resources", response_model=list[schemas.ResourceOut])
def list_resources(topic_id: int, db: Session = Depends(get_db)):
    return db.query(models.Resource).filter(models.Resource.topic_id == topic_id).order_by(models.Resource.id).all()


@router.get("/{topic_id}/diagrams", response_model=list[schemas.DiagramOut])
def list_diagrams(topic_id: int, db: Session = Depends(get_db)):
    return db.query(models.Diagram).filter(models.Diagram.topic_id == topic_id).order_by(models.Diagram.id).all()


@router.get("/{topic_id}/concepts", response_model=list[schemas.ConceptTermOut])
def list_concepts(topic_id: int, db: Session = Depends(get_db)):
    return db.query(models.ConceptTerm).filter(models.ConceptTerm.topic_id == topic_id).order_by(models.ConceptTerm.id).all()


@router.patch("/{topic_id}/concepts/{concept_id}", response_model=schemas.ConceptTermOut)
def update_concept(
    topic_id: int,
    concept_id: int,
    payload: schemas.ConceptTermUpdate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    concept = db.get(models.ConceptTerm, concept_id)
    if not concept or concept.topic_id != topic_id:
        raise HTTPException(404, "Concept not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(concept, field, value)
    db.commit()
    db.refresh(concept)
    return concept
