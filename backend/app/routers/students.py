from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db

router = APIRouter(prefix="/api/students", tags=["students"])


@router.get("", response_model=list[schemas.StudentOut])
def list_students(db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    """Shared roster, like topics -- any coach can see every student, not
    just ones they personally added."""
    students = db.query(models.Student).order_by(models.Student.name).all()
    return [schemas.StudentOut.from_model(s) for s in students]


@router.post("", response_model=schemas.StudentOut)
def add_student(
    payload: schemas.StudentCreate, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    email = payload.email.strip().lower()
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        raise HTTPException(400, "Enter a valid email address.")
    if db.query(models.Student).filter(models.Student.email == email).first():
        raise HTTPException(409, "That email has already been added.")

    student = models.Student(name=payload.name.strip(), email=email, added_by_coach_id=coach.id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return schemas.StudentOut.from_model(student)


@router.put("/{student_id}/topics", response_model=schemas.StudentOut)
def set_student_topics(
    student_id: int,
    payload: schemas.StudentTopicsUpdate,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Replaces this student's whole assigned-topics set with payload.topic_ids
    -- the roster page's checklist always submits the full set, not a diff."""
    student = db.get(models.Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")

    db.query(models.StudentTopic).filter(models.StudentTopic.student_id == student_id).delete()
    for topic_id in set(payload.topic_ids):
        db.add(models.StudentTopic(student_id=student_id, topic_id=topic_id))
    db.commit()
    db.refresh(student)
    return schemas.StudentOut.from_model(student)
