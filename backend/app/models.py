import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


def now() -> datetime.datetime:
    return datetime.datetime.utcnow()


class Coach(Base):
    __tablename__ = "coaches"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    # Filled in from the Google profile on first sign-in. NULL until then --
    # a row with google_sub IS NULL means "invited, hasn't signed in yet".
    name: Mapped[str | None] = mapped_column(String(200), nullable=True)
    google_sub: Mapped[str | None] = mapped_column(String(64), unique=True, nullable=True)
    invited_by_coach_id: Mapped[int | None] = mapped_column(ForeignKey("coaches.id"), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)
    # NULL provider = use the app's shared default (Gemini) key -- today's
    # behavior, unchanged. Non-NULL means this coach brought their own
    # provider + key (see app/llm/router.py); the key itself is Fernet-
    # encrypted at rest (app/crypto.py), never stored or returned in plaintext.
    llm_provider: Mapped[str | None] = mapped_column(String(20), nullable=True)
    llm_api_key_encrypted: Mapped[str | None] = mapped_column(Text, nullable=True)


class CoachSession(Base):
    __tablename__ = "coach_sessions"

    token: Mapped[str] = mapped_column(String(64), primary_key=True)
    coach_id: Mapped[int] = mapped_column(ForeignKey("coaches.id"))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)
    expires_at: Mapped[datetime.datetime] = mapped_column(DateTime)


class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_name: Mapped[str] = mapped_column(String(200))
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(Text, default="")
    created_by_coach_id: Mapped[int | None] = mapped_column(ForeignKey("coaches.id"), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)
    # Gates student visibility of concepts/story, independent of each
    # concept's own `approved` flag -- lets a coach approve concepts
    # incrementally while iterating, then flip this once ready.
    content_published: Mapped[bool] = mapped_column(Boolean, default=False)
    # One narrative per topic (not per concept) weaving approved concepts
    # together -- generated only when a coach explicitly asks for it.
    story_md: Mapped[str] = mapped_column(Text, default="")

    resources: Mapped[list["Resource"]] = relationship(back_populates="topic", cascade="all, delete-orphan")
    concepts: Mapped[list["ConceptTerm"]] = relationship(back_populates="topic", cascade="all, delete-orphan")
    assessments: Mapped[list["Assessment"]] = relationship(back_populates="topic", cascade="all, delete-orphan")
    # Named created_by_coach (not created_by) so it doesn't collide with
    # TopicOut.created_by (a plain string) when Pydantic validates from
    # attributes -- schemas.py resolves the name explicitly in from_model().
    created_by_coach: Mapped["Coach | None"] = relationship(foreign_keys=[created_by_coach_id])


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    type: Mapped[str] = mapped_column(String(20))  # video | text | link | pdf | research
    title: Mapped[str] = mapped_column(String(300), default="")
    source_url: Mapped[str] = mapped_column(String(1000), default="")
    raw_text: Mapped[str] = mapped_column(Text, default="")
    transcript: Mapped[str] = mapped_column(Text, default="")
    status: Mapped[str] = mapped_column(String(20), default="ready")  # pending | ready | failed
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)

    topic: Mapped["Topic"] = relationship(back_populates="resources")


class ConceptTerm(Base):
    __tablename__ = "concept_terms"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    term: Mapped[str] = mapped_column(String(300))
    explanation_md: Mapped[str] = mapped_column(Text, default="")
    # Short relatable comparison generated alongside explanation_md -- the
    # "back of the flashcard" content beyond the plain explanation.
    analogy: Mapped[str] = mapped_column(Text, default="")
    source_resource_ids: Mapped[list] = mapped_column(JSON, default=list)
    video_relevant: Mapped[bool] = mapped_column(Boolean, default=False)
    approved: Mapped[bool] = mapped_column(Boolean, default=False)
    # Data URL (data:image/png;base64,...) for the review agent's generated
    # flashcard illustration -- stored inline rather than in blob storage,
    # fine at this app's scale (see README).
    image_data_url: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)

    topic: Mapped["Topic"] = relationship(back_populates="concepts")


class Assessment(Base):
    __tablename__ = "assessments"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    status: Mapped[str] = mapped_column(String(20), default="draft")  # draft | published
    created_by_coach_id: Mapped[int | None] = mapped_column(ForeignKey("coaches.id"), nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)

    topic: Mapped["Topic"] = relationship(back_populates="assessments")
    questions: Mapped[list["Question"]] = relationship(back_populates="assessment", cascade="all, delete-orphan", order_by="Question.order")
    created_by_coach: Mapped["Coach | None"] = relationship(foreign_keys=[created_by_coach_id])


class Question(Base):
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(primary_key=True)
    assessment_id: Mapped[int] = mapped_column(ForeignKey("assessments.id"))
    prompt: Mapped[str] = mapped_column(Text)
    type: Mapped[str] = mapped_column(String(20))  # mcq | short
    choices: Mapped[list] = mapped_column(JSON, default=list)
    correct_answer: Mapped[str] = mapped_column(Text)
    explanation: Mapped[str] = mapped_column(Text, default="")
    order: Mapped[int] = mapped_column(Integer, default=0)

    assessment: Mapped["Assessment"] = relationship(back_populates="questions")


class Attempt(Base):
    __tablename__ = "attempts"

    id: Mapped[int] = mapped_column(primary_key=True)
    assessment_id: Mapped[int] = mapped_column(ForeignKey("assessments.id"))
    student_name: Mapped[str] = mapped_column(String(200))
    started_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)
    submitted_at: Mapped[datetime.datetime | None] = mapped_column(DateTime, nullable=True)
    score: Mapped[float | None] = mapped_column(nullable=True)

    answers: Mapped[list["AttemptAnswer"]] = relationship(back_populates="attempt", cascade="all, delete-orphan")


class AttemptAnswer(Base):
    __tablename__ = "attempt_answers"

    id: Mapped[int] = mapped_column(primary_key=True)
    attempt_id: Mapped[int] = mapped_column(ForeignKey("attempts.id"))
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"))
    student_answer: Mapped[str] = mapped_column(Text, default="")
    is_correct: Mapped[bool | None] = mapped_column(nullable=True)
    hints_used: Mapped[int] = mapped_column(Integer, default=0)

    attempt: Mapped["Attempt"] = relationship(back_populates="answers")
    tutor_messages: Mapped[list["TutorMessage"]] = relationship(back_populates="attempt_answer", cascade="all, delete-orphan")


class TutorMessage(Base):
    __tablename__ = "tutor_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    attempt_answer_id: Mapped[int] = mapped_column(ForeignKey("attempt_answers.id"))
    role: Mapped[str] = mapped_column(String(20))  # user | assistant
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)

    attempt_answer: Mapped["AttemptAnswer"] = relationship(back_populates="tutor_messages")


class TopicChatMessage(Base):
    __tablename__ = "topic_chat_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))
    # Exactly one of coach_id/session_token is set per row -- coach_id for an
    # authenticated coach's own conversation, session_token (a UUID the
    # frontend generates and stores in localStorage) for an anonymous
    # student's, since students have no account in this app. Enforced by the
    # router, not a DB constraint -- this file doesn't use CheckConstraint
    # anywhere else.
    coach_id: Mapped[int | None] = mapped_column(ForeignKey("coaches.id"), nullable=True)
    session_token: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    role: Mapped[str] = mapped_column(String(20))  # user | assistant
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=now)
