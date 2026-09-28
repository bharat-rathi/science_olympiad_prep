import datetime
import secrets

from authlib.integrations.starlette_client import OAuth
from fastapi import HTTPException, Request, Response
from sqlalchemy.orm import Session

from app import models
from app.config import settings

SESSION_COOKIE_NAME = "sciolympiad_session"
SESSION_TTL_DAYS = 30

# Coach identity is Google-only (see routers/auth.py for the login/callback
# routes). Registered here, alongside the session helpers below, since both
# are "how a request gets a coach attached to it".
oauth = OAuth()
oauth.register(
    name="google",
    client_id=settings.google_client_id,
    client_secret=settings.google_client_secret,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)


def set_session_cookie(response: Response, request: Request, token: str) -> None:
    """Shared by both coach and student sessions (both sign in through the
    same Google OAuth callback, see routers/auth.py) -- one cookie regardless
    of which kind of session it points to."""
    response.set_cookie(
        SESSION_COOKIE_NAME,
        token,
        max_age=SESSION_TTL_DAYS * 24 * 3600,
        httponly=True,
        samesite="lax",
        secure=request.url.scheme == "https",
    )


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


def create_student_session(db: Session, student: models.Student) -> str:
    token = secrets.token_urlsafe(32)
    session = models.StudentSession(
        token=token,
        student_id=student.id,
        expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=SESSION_TTL_DAYS),
    )
    db.add(session)
    db.commit()
    return token


def get_student_from_token(db: Session, token: str) -> models.Student | None:
    session = db.get(models.StudentSession, token)
    if session is None:
        return None
    if session.expires_at < datetime.datetime.utcnow():
        db.delete(session)
        db.commit()
        return None
    return db.get(models.Student, session.student_id)


def delete_any_session(db: Session, token: str) -> None:
    """Logout doesn't know in advance whether the cookie belongs to a coach
    or a student -- try both; at most one will ever match."""
    delete_session(db, token)
    session = db.get(models.StudentSession, token)
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


def require_topic_visible(db: Session, request: Request, topic_id: int) -> models.Topic:
    """Every topic-scoped, student-reachable endpoint calls this instead of a
    bare db.get(Topic, ...). A coach can see every topic, unchanged; a
    student can only see topics a coach has explicitly assigned them
    (models.StudentTopic, set from the roster page's per-student checklist).
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    student = request.state.student
    if student is not None:
        assigned = (
            db.query(models.StudentTopic)
            .filter_by(student_id=student.id, topic_id=topic_id)
            .first()
        )
        if assigned is None:
            raise HTTPException(403, "You don't have access to this topic.")
    return topic
