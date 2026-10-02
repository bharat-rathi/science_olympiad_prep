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


def is_open_to_all_students(topic: models.Topic) -> bool:
    """App-shipped deterministic chapters (Topic.open_to_all_students) are
    visible to every student without a roster assignment, as long as they're
    still published."""
    return bool(topic.open_to_all_students and topic.content_published)


def open_chapter_parent_ids(db: Session) -> set[int]:
    """Events that hold at least one published open-to-all chapter. Students
    reach those chapters THROUGH their event (e.g. Solar System), so the
    event itself is visible to every student too."""
    rows = (
        db.query(models.Topic.parent_topic_id)
        .filter(
            models.Topic.parent_topic_id.isnot(None),
            models.Topic.open_to_all_students.is_(True),
            models.Topic.content_published.is_(True),
        )
        .distinct()
    )
    return {row[0] for row in rows}


def student_can_see(db: Session, student: models.Student, topic: models.Topic) -> bool:
    if is_open_to_all_students(topic) or topic.id in open_chapter_parent_ids(db):
        return True
    return (
        db.query(models.StudentTopic).filter_by(student_id=student.id, topic_id=topic.id).first() is not None
    )


def require_topic_visible(db: Session, request: Request, topic_id: int) -> models.Topic:
    """Every topic-scoped, student-reachable endpoint calls this instead of a
    bare db.get(Topic, ...). A coach can see every topic, unchanged; a
    student can see topics a coach has explicitly assigned them
    (models.StudentTopic, set from the roster page's per-student checklist),
    plus published open-to-all chapters and the events that hold them (see
    student_can_see).
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")
    student = request.state.student
    if student is not None and not student_can_see(db, student, topic):
        raise HTTPException(403, "You don't have access to this topic.")
    return topic
