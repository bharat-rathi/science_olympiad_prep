from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db

router = APIRouter(prefix="/api/topics", tags=["topics"])


@router.get("", response_model=list[schemas.TopicOut])
def list_topics(request: Request, db: Session = Depends(get_db)):
    query = db.query(models.Topic)
    student = request.state.student
    if student is not None:
        # A student only ever sees topics a coach has explicitly assigned
        # them (models.StudentTopic) -- coaches still see everything.
        assigned_ids = [
            row.topic_id for row in db.query(models.StudentTopic).filter(models.StudentTopic.student_id == student.id)
        ]
        query = query.filter(models.Topic.id.in_(assigned_ids))
    topics = query.order_by(models.Topic.id).all()
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
def get_topic(topic_id: int, request: Request, db: Session = Depends(get_db)):
    topic = auth.require_topic_visible(db, request, topic_id)
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
def list_resources(topic_id: int, request: Request, db: Session = Depends(get_db)):
    auth.require_topic_visible(db, request, topic_id)
    return db.query(models.Resource).filter(models.Resource.topic_id == topic_id).order_by(models.Resource.id).all()


@router.get("/{topic_id}/diagrams", response_model=list[schemas.DiagramOut])
def list_diagrams(topic_id: int, request: Request, db: Session = Depends(get_db)):
    auth.require_topic_visible(db, request, topic_id)
    return db.query(models.Diagram).filter(models.Diagram.topic_id == topic_id).order_by(models.Diagram.id).all()


@router.get("/{topic_id}/concepts", response_model=list[schemas.ConceptTermOut])
def list_concepts(topic_id: int, request: Request, db: Session = Depends(get_db)):
    auth.require_topic_visible(db, request, topic_id)
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


@router.get("/{topic_id}/schedule", response_model=list[schemas.ScheduleEntryOut])
def list_schedule(topic_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.ScheduleEntry)
        .filter(models.ScheduleEntry.topic_id == topic_id)
        .order_by(models.ScheduleEntry.scheduled_at)
        .all()
    )


@router.post("/{topic_id}/schedule", response_model=schemas.ScheduleEntryOut)
def create_schedule_entry(
    topic_id: int,
    payload: schemas.ScheduleEntryCreate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    entry = models.ScheduleEntry(topic_id=topic_id, created_by_coach_id=coach.id, **payload.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/{topic_id}/schedule/{entry_id}", status_code=204)
def delete_schedule_entry(
    topic_id: int, entry_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    entry = db.get(models.ScheduleEntry, entry_id)
    if not entry or entry.topic_id != topic_id:
        raise HTTPException(404, "Schedule entry not found")
    db.delete(entry)
    db.commit()


@router.get("/{topic_id}/sub-topics", response_model=list[schemas.TopicOut])
def list_sub_topics(topic_id: int, db: Session = Depends(get_db)):
    """Sub-topics created for a scheduled deep dive (see ScheduleEntry) --
    just Topic rows with parent_topic_id set to this one."""
    subs = db.query(models.Topic).filter(models.Topic.parent_topic_id == topic_id).order_by(models.Topic.id).all()
    return [schemas.TopicOut.from_model(t) for t in subs]
