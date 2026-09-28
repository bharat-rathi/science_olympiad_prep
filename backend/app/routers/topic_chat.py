from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db
from app.llm.prompts import topic_qa_system_prompt
from app.llm.router import get_llm_handle
from app.rag.retrieval import retrieve_chunks_for_message

router = APIRouter(prefix="/api/topics", tags=["topic_chat"])


def _identity(request: Request) -> tuple[models.Coach | None, dict]:
    """Resolve who's chatting: the logged-in coach or student (session
    cookie, resolved into request.state by attach_identity in main.py --
    everyone chats logged in now, no more anonymous session_token). Exactly
    one of coach_id/student_id comes back set, for filtering/tagging
    TopicChatMessage rows. Returns the coach separately (or None) since
    get_llm_handle only takes a Coach -- students don't have personal LLM
    provider settings, so they always use the shared default key.
    """
    coach = request.state.coach
    if coach is not None:
        return coach, {"coach_id": coach.id, "student_id": None}
    student = request.state.student
    if student is not None:
        return None, {"coach_id": None, "student_id": student.id}
    raise HTTPException(401, "Log in to chat about this topic.")


@router.get("/{topic_id}/chat", response_model=list[schemas.TopicChatMessageOut])
def get_topic_chat(topic_id: int, request: Request, db: Session = Depends(get_db)):
    auth.require_topic_visible(db, request, topic_id)
    _, ident = _identity(request)
    return (
        db.query(models.TopicChatMessage)
        .filter_by(topic_id=topic_id, **ident)
        .order_by(models.TopicChatMessage.id)
        .all()
    )


@router.post("/{topic_id}/chat/turn", response_model=schemas.TopicChatMessageOut)
def topic_chat_turn(topic_id: int, payload: schemas.TopicChatTurnRequest, request: Request, db: Session = Depends(get_db)):
    topic = auth.require_topic_visible(db, request, topic_id)
    coach, ident = _identity(request)

    db.add(models.TopicChatMessage(topic_id=topic_id, role="user", content=payload.message, **ident))
    db.commit()

    chunks = retrieve_chunks_for_message(payload.message, topic_id)
    labeled = [{"source_type": c["metadata"]["source_type"], "text": c["text"]} for c in chunks]
    system = topic_qa_system_prompt(topic.name, labeled)

    history = [
        {"role": m.role, "content": m.content}
        for m in db.query(models.TopicChatMessage).filter_by(topic_id=topic_id, **ident).order_by(models.TopicChatMessage.id).all()
    ]
    reply = get_llm_handle(coach).chat_turn(system, history, max_tokens=800, effort="low", label="topic_chat_turn")

    assistant_msg = models.TopicChatMessage(topic_id=topic_id, role="assistant", content=reply, **ident)
    db.add(assistant_msg)
    db.commit()
    db.refresh(assistant_msg)
    return assistant_msg
