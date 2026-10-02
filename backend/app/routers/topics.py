from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db

router = APIRouter(prefix="/api/topics", tags=["topics"])


@router.get("", response_model=list[schemas.TopicOut])
def list_topics(request: Request, db: Session = Depends(get_db), include_sub_topics: bool = False):
    query = db.query(models.Topic)
    student = request.state.student
    if student is not None:
        # A student sees topics a coach has explicitly assigned them
        # (models.StudentTopic) plus published open-to-all topics (app-shipped
        # deterministic chapters, see auth.is_open_to_all_students) --
        # coaches still see everything, subject to include_sub_topics below.
        # A student can be assigned a specific chapter directly, so this
        # branch is never further restricted to top-level topics.
        assigned_ids = [
            row.topic_id for row in db.query(models.StudentTopic).filter(models.StudentTopic.student_id == student.id)
        ]
        query = query.filter(
            or_(
                models.Topic.id.in_(assigned_ids),
                and_(models.Topic.open_to_all_students.is_(True), models.Topic.content_published.is_(True)),
            )
        )
    elif not include_sub_topics:
        # Default coach view (e.g. the Home page grid) shows events only --
        # each event's chapters are reached by drilling into its own
        # "Chapters" section (CoachTopicBuilder.tsx), not as separate flat
        # entries here. Pass include_sub_topics=true (e.g. the student
        # roster's per-topic assignment checklist) to get the full flat
        # list, chapters included, when that's genuinely useful.
        query = query.filter(models.Topic.parent_topic_id.is_(None))
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


@router.post("/{topic_id}/concepts/branch", response_model=schemas.TopicOut)
def branch_concepts(
    topic_id: int,
    payload: schemas.BranchConceptsRequest,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Splits already-generated concepts out of a big topic into a new
    sub-topic, for a coach who taught everything as one blob and now wants
    to teach it across separate sessions -- moves the selected ConceptTerm
    rows (not a copy), so they stop appearing under the original topic.
    Resources/diagrams stay on the parent (shared source material); only
    the organized teaching units move.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    if not payload.new_topic_name.strip():
        raise HTTPException(400, "Enter a name for the new sub-topic.")
    if not payload.concept_ids:
        raise HTTPException(400, "Select at least one concept to branch.")

    concepts = (
        db.query(models.ConceptTerm)
        .filter(models.ConceptTerm.id.in_(payload.concept_ids), models.ConceptTerm.topic_id == topic_id)
        .all()
    )
    if len(concepts) != len(set(payload.concept_ids)):
        raise HTTPException(404, "One or more concepts weren't found on this topic.")

    sub_topic = models.Topic(
        event_name=topic.event_name,
        name=payload.new_topic_name.strip(),
        assessment_type=topic.assessment_type,
        parent_topic_id=topic.id,
        created_by_coach_id=coach.id,
    )
    db.add(sub_topic)
    db.flush()

    for concept in concepts:
        concept.topic_id = sub_topic.id

    db.commit()
    db.refresh(sub_topic)
    return schemas.TopicOut.from_model(sub_topic)
