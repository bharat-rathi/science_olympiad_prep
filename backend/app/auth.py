import datetime
import secrets

import bcrypt
from fastapi import HTTPException, Request
from sqlalchemy.orm import Session

from app import models

SESSION_COOKIE_NAME = "sciolympiad_session"
SESSION_TTL_DAYS = 30


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
    except ValueError:
        # Malformed stored hash -- treat as a failed login rather than a 500.
        return False


def create_session(db: Session, coach: models.Coach) -> str:
    token = secrets.token_urlsafe(32)
    session = models.CoachSession(
        token=token,
        coach_id=coach.id,
        expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=SESSION_TTL_DAYS),
    )
    db.add(session)
    db.commit()
    return token


def get_coach_from_token(db: Session, token: str) -> models.Coach | None:
    session = db.get(models.CoachSession, token)
    if session is None:
        return None
    if session.expires_at < datetime.datetime.utcnow():
        db.delete(session)
        db.commit()
        return None
    return db.get(models.Coach, session.coach_id)


def delete_session(db: Session, token: str) -> None:
    session = db.get(models.CoachSession, token)
    if session is not None:
        db.delete(session)
        db.commit()


def require_coach(request: Request) -> models.Coach:
    """FastAPI dependency for coach-only (content-authoring) endpoints.

    Deliberately narrow: only routes that create/edit/publish topic content
    depend on this. Student-facing endpoints (browsing topics, taking an
    assessment, hints, tutor chat) stay public -- students don't have coach
    accounts. `request.state.coach` is populated for every request by the
    attach_coach_session middleware in main.py regardless of whether this
    dependency is used.
    """
    if request.state.coach is None:
        raise HTTPException(401, "Log in as a coach to do this")
    return request.state.coach
