from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db
from app.llm.client import complete_json
from app.llm.prompts import QUIZ_SCHEMA, quiz_prompt

router = APIRouter(prefix="/api", tags=["assessment"])


@router.post("/topics/{topic_id}/assessment", response_model=schemas.AssessmentOut)
def get_or_create_draft_assessment(
    topic_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    """Entry point for the assessment editor -- no LLM call.

    Returns the topic's existing draft assessment if there is one, otherwise
    creates an empty one. The coach fills it in from here via
    generate-questions (AI-suggested) and/or manually added questions.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    draft = (
        db.query(models.Assessment)
        .filter(models.Assessment.topic_id == topic_id, models.Assessment.status == "draft")
        .order_by(models.Assessment.id.desc())
        .first()
    )
    if draft:
        return schemas.AssessmentOut.from_model(draft)

    draft = models.Assessment(topic_id=topic_id, status="draft", created_by_coach_id=coach.id)
    db.add(draft)
    db.commit()
    db.refresh(draft)
    return schemas.AssessmentOut.from_model(draft)


@router.post("/assessments/{assessment_id}/generate-questions", response_model=schemas.AssessmentOut)
def generate_questions(
    assessment_id: int,
    payload: schemas.GenerateQuestionsRequest,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Coach picks the mix; the LLM appends that many questions to the existing draft."""
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    if payload.num_mcq <= 0 and payload.num_short <= 0:
        return schemas.AssessmentOut.from_model(assessment)

    approved = db.query(models.ConceptTerm).filter(
        models.ConceptTerm.topic_id == assessment.topic_id, models.ConceptTerm.approved.is_(True)
    ).all()
    if not approved:
        raise HTTPException(400, "No approved concepts yet -- approve at least one before generating questions")

    system, user = quiz_prompt(
        assessment.topic.name,
        [{"term": c.term, "explanation_md": c.explanation_md} for c in approved],
        payload.num_mcq,
        payload.num_short,
    )
    result = complete_json(
        system, user, QUIZ_SCHEMA, max_tokens=4000, effort="high", label="generate_assessment_questions"
    )

    next_order = max((q.order for q in assessment.questions), default=-1) + 1
    for i, q in enumerate(result.get("questions", [])):
        db.add(
            models.Question(
                assessment_id=assessment.id,
                prompt=q["prompt"],
                type=q["type"],
                choices=q["choices"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"],
                order=next_order + i,
            )
        )
    db.commit()
    db.refresh(assessment)
    return schemas.AssessmentOut.from_model(assessment)


@router.post("/assessments/{assessment_id}/questions", response_model=schemas.QuestionOut)
def add_question(
    assessment_id: int,
    payload: schemas.QuestionCreate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Coach manually authors a question -- no LLM involved."""
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    if payload.type not in ("mcq", "short"):
        raise HTTPException(400, "type must be 'mcq' or 'short'")

    next_order = max((q.order for q in assessment.questions), default=-1) + 1
    question = models.Question(
        assessment_id=assessment_id,
        prompt=payload.prompt,
        type=payload.type,
        choices=payload.choices,
        correct_answer=payload.correct_answer,
        explanation=payload.explanation,
        order=next_order,
    )
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


@router.get("/topics/{topic_id}/assessment", response_model=schemas.AssessmentOut | None)
def get_latest_assessment(topic_id: int, db: Session = Depends(get_db)):
    assessment = (
        db.query(models.Assessment)
        .filter(models.Assessment.topic_id == topic_id)
        .order_by(models.Assessment.id.desc())
        .first()
    )
    return schemas.AssessmentOut.from_model(assessment) if assessment else None


@router.get("/assessments/{assessment_id}", response_model=schemas.AssessmentOut)
def get_assessment(assessment_id: int, db: Session = Depends(get_db)):
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    return schemas.AssessmentOut.from_model(assessment)


@router.post("/assessments/{assessment_id}/publish", response_model=schemas.AssessmentOut)
def publish_assessment(
    assessment_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    assessment.status = "published"
    db.commit()
    db.refresh(assessment)
    return schemas.AssessmentOut.from_model(assessment)


@router.patch("/assessments/{assessment_id}/questions/{question_id}", response_model=schemas.QuestionOut)
def update_question(
    assessment_id: int,
    question_id: int,
    payload: schemas.QuestionUpdate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    question = db.get(models.Question, question_id)
    if not question or question.assessment_id != assessment_id:
        raise HTTPException(404, "Question not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(question, field, value)
    db.commit()
    db.refresh(question)
    return question


@router.delete("/assessments/{assessment_id}/questions/{question_id}")
def delete_question(
    assessment_id: int, question_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    question = db.get(models.Question, question_id)
    if not question or question.assessment_id != assessment_id:
        raise HTTPException(404, "Question not found")
    db.delete(question)
    db.commit()
    return {"ok": True}
