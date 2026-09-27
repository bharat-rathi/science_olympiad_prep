import re

from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session

from app import auth, models, passwords, schemas
from app.db import get_db

router = APIRouter(prefix="/api/students", tags=["students"])

_USERNAME_RE = re.compile(r"^[a-z0-9._-]{3,64}$")


@router.get("", response_model=list[schemas.StudentOut])
def list_students(db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    """Shared roster, like topics -- any coach can see every student, not
    just ones they personally added."""
    return db.query(models.Student).order_by(models.Student.name).all()


@router.post("", response_model=schemas.StudentCreated)
def add_student(
    payload: schemas.StudentCreate, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)
):
    username = payload.username.strip().lower()
    if not _USERNAME_RE.match(username):
        raise HTTPException(400, "Username must be 3-64 characters: lowercase letters, numbers, dots, dashes, or underscores.")
    if db.query(models.Student).filter(models.Student.username == username).first():
        raise HTTPException(409, "That username is already taken.")

    pin = passwords.generate_pin()
    student = models.Student(
        name=payload.name.strip(),
        username=username,
        password_hash=passwords.hash_password(pin),
        added_by_coach_id=coach.id,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return schemas.StudentCreated(student=student, pin=pin)


@router.post("/{student_id}/reset-pin", response_model=schemas.StudentCreated)
def reset_pin(student_id: int, db: Session = Depends(get_db), coach: models.Coach = Depends(auth.require_coach)):
    student = db.get(models.Student, student_id)
    if not student:
        raise HTTPException(404, "Student not found")
    pin = passwords.generate_pin()
    student.password_hash = passwords.hash_password(pin)
    db.commit()
    db.refresh(student)
    return schemas.StudentCreated(student=student, pin=pin)


@router.post("/login", response_model=schemas.StudentOut)
def student_login(payload: schemas.StudentLoginRequest, request: Request, response: Response, db: Session = Depends(get_db)):
    username = payload.username.strip().lower()
    student = db.query(models.Student).filter(models.Student.username == username).first()
    if not student or not passwords.verify_password(payload.pin, student.password_hash):
        raise HTTPException(401, "Incorrect username or PIN.")

    session_token = auth.create_student_session(db, student)
    auth.set_session_cookie(response, request, session_token)
    return student
