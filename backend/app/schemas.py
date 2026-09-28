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


class StudentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    email: str
    created_at: datetime.datetime
    topic_ids: list[int] = []

    @staticmethod
    def from_model(student) -> "StudentOut":
        out = StudentOut.model_validate(student)
        out.topic_ids = [t.id for t in student.assigned_topics]
        return out


class StudentCreate(BaseModel):
    name: str
    email: str


class StudentTopicsUpdate(BaseModel):
    topic_ids: list[int]


class AiSettingsOut(BaseModel):
    provider: str | None = None
    has_key: bool = False


class AiSettingsUpdate(BaseModel):
    provider: str | None = None
    api_key: str | None = None


class MeResponse(BaseModel):
    authenticated: bool
    coach: CoachOut | None = None
    student: StudentOut | None = None
    needs_bootstrap: bool = False


class DriveStatusOut(BaseModel):
    connected: bool


class TopicOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    event_name: str
    name: str
    description: str
    assessment_type: str = "test"
    parent_topic_id: int | None = None
    created_at: datetime.datetime
    created_by: str | None = None
    content_published: bool = False
    story_md: str = ""
    overview_what: str = ""
    overview_learn: str = ""
    overview_assessed: str = ""
    overview_theme_2027: str = ""
    overview_notes: str = ""

    @staticmethod
    def from_model(topic) -> "TopicOut":
        out = TopicOut.model_validate(topic)
        out.created_by = topic.created_by_coach.name if topic.created_by_coach else None
        return out


class TopicCreate(BaseModel):
    event_name: str
    name: str
    description: str = ""
    assessment_type: str = "test"
    parent_topic_id: int | None = None


class TopicStoryUpdate(BaseModel):
    story_md: str


class ScheduleEntryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    scheduled_at: datetime.datetime
    title: str
    notes: str
    created_at: datetime.datetime


class ScheduleEntryCreate(BaseModel):
    scheduled_at: datetime.datetime
    title: str = ""
    notes: str = ""


class BranchConceptsRequest(BaseModel):
    concept_ids: list[int]
    new_topic_name: str


class ResourceOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    type: str
    title: str
    source_url: str
    status: str
    created_at: datetime.datetime
    raw_text: str = ""
    transcript: str = ""
    error_message: str = ""


class ResourceCreateText(BaseModel):
    title: str
    text: str
    source_url: str = ""


class ResourceCreateLink(BaseModel):
    # Despite the name, this doubles as a research-agent trigger: ingestion.py
    # only treats it as a URL to fetch if it parses as one, otherwise it's
    # handed to the research agent as a search keyword/topic.
    url: str


class DiagramOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    resource_id: int
    image_data_url: str
    caption: str
    page_number: int


class ConceptTermOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    topic_id: int
    term: str
    explanation_md: str
    analogy: str = ""
    why_it_matters: str = ""
    source_resource_ids: list[int]
    video_relevant: bool
    approved: bool
    image_data_url: str = ""


class ConceptTermUpdate(BaseModel):
    term: str | None = None
    explanation_md: str | None = None
    analogy: str | None = None
    why_it_matters: str | None = None
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


class TopicChatMessageOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    role: str
    content: str
    created_at: datetime.datetime


class TopicChatTurnRequest(BaseModel):
    message: str
