from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.llm.prompts import topic_qa_system_prompt
from app.llm.router import get_llm_handle
from app.rag.retrieval import retrieve_chunks_for_message

router = APIRouter(prefix="/api/topics", tags=["topic_chat"])


def _identity(request: Request, session_token: str | None) -> tuple["models.Coach | None", dict]:
    """Resolve who's chatting: the logged-in coach (from the session cookie
    the attach_coach_session middleware already resolved), or an anonymous
    student identified by a client-generated session_token. Exactly one of
    coach_id/session_token comes back set, for filtering/tagging TopicChatMessage rows.
    """
    coach = request.state.coach
    if coach is not None:
        return coach, {"coach_id": coach.id, "session_token": None}
    if not session_token:
        raise HTTPException(400, "session_token is required")
    return None, {"coach_id": None, "session_token": session_token}


@router.get("/{topic_id}/chat", response_model=list[schemas.TopicChatMessageOut])
def get_topic_chat(topic_id: int, request: Request, session_token: str | None = None, db: Session = Depends(get_db)):
    _, ident = _identity(request, session_token)
    return (
        db.query(models.TopicChatMessage)
        .filter_by(topic_id=topic_id, **ident)
        .order_by(models.TopicChatMessage.id)
        .all()
    )


@router.post("/{topic_id}/chat/turn", response_model=schemas.TopicChatMessageOut)
def topic_chat_turn(topic_id: int, payload: schemas.TopicChatTurnRequest, request: Request, db: Session = Depends(get_db)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    coach, ident = _identity(request, payload.session_token)

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
