from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.llm.client import chat_turn
from app.llm.prompts import tutor_system_prompt

router = APIRouter(prefix="/api", tags=["tutor"])


def _get_attempt_answer(db: Session, attempt_id: int, question_id: int) -> models.AttemptAnswer:
    row = (
        db.query(models.AttemptAnswer)
        .filter(models.AttemptAnswer.attempt_id == attempt_id, models.AttemptAnswer.question_id == question_id)
        .first()
    )
    if not row:
        raise HTTPException(404, "No answer recorded for this question yet -- submit the attempt first")
    return row


def _system_prompt(db: Session, row: models.AttemptAnswer) -> str:
    question = db.get(models.Question, row.question_id)
    topic = question.assessment.topic
    context = "\n\n".join(
        f"### {c.term}\n{c.explanation_md}"
        for c in db.query(models.ConceptTerm).filter(
            models.ConceptTerm.topic_id == topic.id, models.ConceptTerm.approved.is_(True)
        )
    )
    return tutor_system_prompt(topic.name, context, question.prompt, question.correct_answer, row.student_answer)


@router.get("/attempts/{attempt_id}/questions/{question_id}/tutor", response_model=list[schemas.TutorMessageOut])
def get_tutor_thread(attempt_id: int, question_id: int, db: Session = Depends(get_db)):
    row = _get_attempt_answer(db, attempt_id, question_id)
    return row.tutor_messages


@router.post("/attempts/{attempt_id}/questions/{question_id}/tutor/start", response_model=schemas.TutorMessageOut)
def start_tutor_thread(attempt_id: int, question_id: int, db: Session = Depends(get_db)):
    row = _get_attempt_answer(db, attempt_id, question_id)
    if row.tutor_messages:
        return row.tutor_messages[-1]

    system = _system_prompt(db, row)
    opening = chat_turn(
        system,
        [{"role": "user", "content": "The student just got this wrong. Start the conversation."}],
        max_tokens=600,
        effort="low",
    )
    msg = models.TutorMessage(attempt_answer_id=row.id, role="assistant", content=opening)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


@router.post("/tutor/turn", response_model=schemas.TutorMessageOut)
def tutor_turn(payload: schemas.TutorTurnRequest, db: Session = Depends(get_db)):
    row = _get_attempt_answer(db, payload.attempt_id, payload.question_id)

    user_msg = models.TutorMessage(attempt_answer_id=row.id, role="user", content=payload.message)
    db.add(user_msg)
    db.commit()

    system = _system_prompt(db, row)
    history = [{"role": m.role, "content": m.content} for m in row.tutor_messages]

    reply = chat_turn(system, history, max_tokens=600, effort="low")
    assistant_msg = models.TutorMessage(attempt_answer_id=row.id, role="assistant", content=reply)
    db.add(assistant_msg)
    db.commit()
    db.refresh(assistant_msg)
    return assistant_msg
