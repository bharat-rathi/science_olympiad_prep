from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.llm.client import complete_json
from app.llm.prompts import QUIZ_SCHEMA, quiz_prompt

router = APIRouter(prefix="/api", tags=["assessment"])


@router.post("/topics/{topic_id}/assessment/generate", response_model=schemas.AssessmentOut)
def generate_assessment(topic_id: int, db: Session = Depends(get_db)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    approved = db.query(models.ConceptTerm).filter(
        models.ConceptTerm.topic_id == topic_id, models.ConceptTerm.approved.is_(True)
    ).all()
    if not approved:
        raise HTTPException(400, "No approved concepts yet -- approve at least one before generating an assessment")

    system, user = quiz_prompt(topic.name, [{"term": c.term, "explanation_md": c.explanation_md} for c in approved])
    result = complete_json(system, user, QUIZ_SCHEMA, max_tokens=4000, effort="high")

    assessment = models.Assessment(topic_id=topic_id, status="draft")
    db.add(assessment)
    db.flush()

    for i, q in enumerate(result.get("questions", [])):
        db.add(
            models.Question(
                assessment_id=assessment.id,
                prompt=q["prompt"],
                type=q["type"],
                choices=q["choices"],
                correct_answer=q["correct_answer"],
                explanation=q["explanation"],
                order=i,
            )
        )
    db.commit()
    db.refresh(assessment)
    return assessment


@router.get("/topics/{topic_id}/assessment", response_model=schemas.AssessmentOut | None)
def get_latest_assessment(topic_id: int, db: Session = Depends(get_db)):
    return (
        db.query(models.Assessment)
        .filter(models.Assessment.topic_id == topic_id)
        .order_by(models.Assessment.id.desc())
        .first()
    )


@router.get("/assessments/{assessment_id}", response_model=schemas.AssessmentOut)
def get_assessment(assessment_id: int, db: Session = Depends(get_db)):
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    return assessment


@router.post("/assessments/{assessment_id}/publish", response_model=schemas.AssessmentOut)
def publish_assessment(assessment_id: int, db: Session = Depends(get_db)):
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    assessment.status = "published"
    db.commit()
    db.refresh(assessment)
    return assessment


@router.patch("/assessments/{assessment_id}/questions/{question_id}", response_model=schemas.QuestionOut)
def update_question(assessment_id: int, question_id: int, payload: schemas.QuestionUpdate, db: Session = Depends(get_db)):
    question = db.get(models.Question, question_id)
    if not question or question.assessment_id != assessment_id:
        raise HTTPException(404, "Question not found")
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(question, field, value)
    db.commit()
    db.refresh(question)
    return question


@router.delete("/assessments/{assessment_id}/questions/{question_id}")
def delete_question(assessment_id: int, question_id: int, db: Session = Depends(get_db)):
    question = db.get(models.Question, question_id)
    if not question or question.assessment_id != assessment_id:
        raise HTTPException(404, "Question not found")
    db.delete(question)
    db.commit()
    return {"ok": True}
