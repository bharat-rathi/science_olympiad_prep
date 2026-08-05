import datetime
import re

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.llm.client import complete_json, complete_text
from app.llm.prompts import hint_prompt

router = APIRouter(prefix="/api", tags=["attempts"])

SHORT_ANSWER_GRADE_SCHEMA = {
    "type": "object",
    "properties": {
        "is_correct": {"type": "boolean"},
        "feedback": {"type": "string"},
    },
    "required": ["is_correct", "feedback"],
    "additionalProperties": False,
}


def _normalize(s: str) -> str:
    return re.sub(r"[^\w\s]", "", s.strip().lower())


def _cheap_match(student_answer: str, correct_answer: str) -> bool:
    """Catch the easy exact/near-exact cases without spending an LLM call.

    Only meant to short-circuit obvious matches -- anything that doesn't
    clear this bar still goes to the LLM grader below, so grading stays
    lenient about phrasing for genuinely ambiguous answers.
    """
    a, b = _normalize(student_answer), _normalize(correct_answer)
    if not a or not b:
        return False
    if a == b:
        return True
    shorter, longer = sorted([a, b], key=len)
    return len(shorter) >= 4 and shorter in longer and len(shorter) / len(longer) >= 0.6


def _topic_concept_context(db: Session, topic_id: int) -> str:
    concepts = db.query(models.ConceptTerm).filter(
        models.ConceptTerm.topic_id == topic_id, models.ConceptTerm.approved.is_(True)
    ).all()
    return "\n\n".join(f"### {c.term}\n{c.explanation_md}" for c in concepts)


@router.post("/assessments/{assessment_id}/attempts", response_model=schemas.AttemptOut)
def start_attempt(assessment_id: int, payload: schemas.AttemptStart, db: Session = Depends(get_db)):
    assessment = db.get(models.Assessment, assessment_id)
    if not assessment:
        raise HTTPException(404, "Assessment not found")
    attempt = models.Attempt(assessment_id=assessment_id, student_name=payload.student_name)
    db.add(attempt)
    db.commit()
    db.refresh(attempt)
    return attempt


@router.post("/attempts/{attempt_id}/hint", response_model=dict)
def request_hint(attempt_id: int, payload: schemas.HintRequest, db: Session = Depends(get_db)):
    attempt = db.get(models.Attempt, attempt_id)
    if not attempt:
        raise HTTPException(404, "Attempt not found")
    question = db.get(models.Question, payload.question_id)
    if not question:
        raise HTTPException(404, "Question not found")
    topic_id = question.assessment.topic_id

    existing = next((a for a in attempt.answers if a.question_id == question.id), None)
    if existing is None:
        existing = models.AttemptAnswer(attempt_id=attempt_id, question_id=question.id, hints_used=0)
        db.add(existing)
    existing.hints_used = (existing.hints_used or 0) + 1

    context = _topic_concept_context(db, topic_id)
    system, user = hint_prompt(question.assessment.topic.name, context, question.prompt)
    hint = complete_text(system, user, max_tokens=500, effort="low", label="hint")

    db.commit()
    return {"hint": hint}


@router.post("/attempts/{attempt_id}/submit", response_model=schemas.AttemptResult)
def submit_attempt(attempt_id: int, payload: schemas.SubmitPayload, db: Session = Depends(get_db)):
    attempt = db.get(models.Attempt, attempt_id)
    if not attempt:
        raise HTTPException(404, "Attempt not found")

    correct_count = 0
    answer_rows = []
    for answer in payload.answers:
        question = db.get(models.Question, answer.question_id)
        if not question:
            continue

        if question.type == "mcq":
            is_correct = answer.student_answer.strip().lower() == question.correct_answer.strip().lower()
        elif _cheap_match(answer.student_answer, question.correct_answer):
            is_correct = True
        else:
            grading = complete_json(
                "You grade a student's short-answer response against the correct answer for a "
                "Science Olympiad practice question. Be lenient about phrasing, strict about substance.",
                f"Question: {question.prompt}\nCorrect answer: {question.correct_answer}\n"
                f"Student answer: {answer.student_answer}",
                SHORT_ANSWER_GRADE_SCHEMA,
                max_tokens=500,
                effort="low",
                label="grade_short_answer",
            )
            is_correct = grading.get("is_correct", False)

        if is_correct:
            correct_count += 1

        row = next((a for a in attempt.answers if a.question_id == answer.question_id), None)
        if row is None:
            row = models.AttemptAnswer(attempt_id=attempt_id, question_id=answer.question_id)
            db.add(row)
        row.student_answer = answer.student_answer
        row.is_correct = is_correct
        answer_rows.append(row)

    attempt.score = correct_count / len(payload.answers) if payload.answers else 0
    attempt.submitted_at = datetime.datetime.utcnow()
    db.commit()
    db.refresh(attempt)
    for row in answer_rows:
        db.refresh(row)

    return schemas.AttemptResult(attempt=attempt, answers=answer_rows)


@router.get("/attempts/{attempt_id}", response_model=schemas.AttemptResult)
def get_attempt(attempt_id: int, db: Session = Depends(get_db)):
    attempt = db.get(models.Attempt, attempt_id)
    if not attempt:
        raise HTTPException(404, "Attempt not found")
    return schemas.AttemptResult(attempt=attempt, answers=attempt.answers)
