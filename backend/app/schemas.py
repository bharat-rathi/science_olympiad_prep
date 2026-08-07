import datetime

from pydantic import BaseModel, ConfigDict


class CoachOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    # NULL for a coach who's been invited (by email) but hasn't signed in
    # with Google yet -- their profile name isn't known until they do.
    name: str | None


class InviteRequest(BaseModel):
    email: str


class MeResponse(BaseModel):
    authenticated: bool
    coach: CoachOut | None = None
    needs_bootstrap: bool = False


class TopicOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    event_name: str
    name: str
    description: str
    created_at: datetime.datetime
    created_by: str | None = None
    content_published: bool = False
    story_md: str = ""

    @staticmethod
    def from_model(topic) -> "TopicOut":
        out = TopicOut.model_validate(topic)
        out.created_by = topic.created_by_coach.name if topic.created_by_coach else None
        return out


class TopicCreate(BaseModel):
    event_name: str
    name: str
    description: str = ""


class TopicStoryUpdate(BaseModel):
    story_md: str


class ResourceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    type: str
    title: str
    source_url: str
    status: str
    created_at: datetime.datetime


class ResourceCreateText(BaseModel):
    title: str
    text: str
    source_url: str = ""


class ResourceCreateLink(BaseModel):
    url: str


class ConceptTermOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    term: str
    explanation_md: str
    analogy: str = ""
    source_resource_ids: list[int]
    video_relevant: bool
    approved: bool


class ConceptTermUpdate(BaseModel):
    term: str | None = None
    explanation_md: str | None = None
    analogy: str | None = None
    approved: bool | None = None


class ConceptFeedbackRequest(BaseModel):
    feedback: str


class QuestionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    assessment_id: int
    prompt: str
    type: str
    choices: list[str]
    correct_answer: str
    explanation: str
    order: int


class QuestionUpdate(BaseModel):
    prompt: str | None = None
    choices: list[str] | None = None
    correct_answer: str | None = None
    explanation: str | None = None
    order: int | None = None


class QuestionCreate(BaseModel):
    prompt: str
    type: str  # mcq | short
    choices: list[str] = []
    correct_answer: str
    explanation: str = ""


class GenerateQuestionsRequest(BaseModel):
    num_mcq: int = 4
    num_short: int = 2


class AssessmentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    status: str
    questions: list[QuestionOut]
    created_by: str | None = None

    @staticmethod
    def from_model(assessment) -> "AssessmentOut":
        out = AssessmentOut.model_validate(assessment)
        out.created_by = assessment.created_by_coach.name if assessment.created_by_coach else None
        return out


class AttemptStart(BaseModel):
    student_name: str


class AttemptOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    assessment_id: int
    student_name: str
    started_at: datetime.datetime
    submitted_at: datetime.datetime | None
    score: float | None


class AnswerSubmit(BaseModel):
    question_id: int
    student_answer: str


class SubmitPayload(BaseModel):
    answers: list[AnswerSubmit]


class AttemptAnswerOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    question_id: int
    student_answer: str
    is_correct: bool | None
    hints_used: int


class AttemptResult(BaseModel):
    attempt: AttemptOut
    answers: list[AttemptAnswerOut]


class HintRequest(BaseModel):
    attempt_id: int
    question_id: int


class TutorMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: str
    content: str
    created_at: datetime.datetime


class TutorTurnRequest(BaseModel):
    attempt_id: int
    question_id: int
    message: str
