import zipfile
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import models, schemas
from app.db import get_db
from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.link_fetch import fetch_url_text
from app.rag.transcription import save_upload_to_temp, transcribe_audio, transcribe_video
from app.rag.vectorstore import add_chunks

router = APIRouter(prefix="/api/topics", tags=["ingestion"])

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".flac"}


def _index_resource(db: Session, resource: models.Resource, text: str) -> None:
    """Chunk + embed a resource's text and store it in the vector DB.

    This is the "ingest" half of the RAG pipeline: raw resource text becomes
    a set of embedded, metadata-tagged chunks that retrieval.py can later
    pull from for a given topic.
    """
    chunks = chunk_text(text)
    if not chunks:
        return
    embeddings = embed_texts(chunks)
    add_chunks(resource.topic_id, resource.id, resource.type, chunks, embeddings)


@router.post("/{topic_id}/resources/text", response_model=schemas.ResourceOut)
def add_text_resource(topic_id: int, payload: schemas.ResourceCreateText, db: Session = Depends(get_db)):
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    resource = models.Resource(
        topic_id=topic_id,
        type="text",
        title=payload.title,
        source_url=payload.source_url,
        raw_text=payload.text,
        status="ready",
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, payload.text)
    return resource


@router.post("/{topic_id}/resources/link", response_model=schemas.ResourceOut)
def add_link_resource(topic_id: int, payload: schemas.ResourceCreateLink, db: Session = Depends(get_db)):
    """Fetch a real URL and ingest its main readable content -- no copy/paste required."""
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    try:
        title, text = fetch_url_text(payload.url)
    except ValueError as e:
        raise HTTPException(422, str(e))

    resource = models.Resource(
        topic_id=topic_id,
        type="link",
        title=title,
        source_url=payload.url,
        raw_text=text,
        status="ready",
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, text)
    return resource


@router.post("/{topic_id}/resources/upload", response_model=list[schemas.ResourceOut])
async def upload_media_resource(topic_id: int, file: UploadFile, db: Session = Depends(get_db)):
    """Upload a video/audio file, or a zip of several, for transcription + ingestion.

    Each video/audio file becomes its own Resource(type="video"); a zip is
    unpacked and each media file inside it is processed the same way.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    data = await file.read()
    filename = file.filename or "upload"
    suffix = Path(filename).suffix.lower()

    created: list[models.Resource] = []
    if suffix == ".zip":
        tmp_zip = save_upload_to_temp(filename, data)
        with zipfile.ZipFile(tmp_zip) as zf:
            for name in zf.namelist():
                ext = Path(name).suffix.lower()
                if ext not in VIDEO_EXTENSIONS | AUDIO_EXTENSIONS:
                    continue
                with zf.open(name) as member:
                    member_bytes = member.read()
                created.append(_transcribe_and_create(db, topic_id, name, member_bytes, ext))
    elif suffix in VIDEO_EXTENSIONS | AUDIO_EXTENSIONS:
        created.append(_transcribe_and_create(db, topic_id, filename, data, suffix))
    else:
        raise HTTPException(400, f"Unsupported file type: {suffix}")

    return created


def _transcribe_and_create(db: Session, topic_id: int, filename: str, data: bytes, ext: str) -> models.Resource:
    tmp_path = save_upload_to_temp(filename, data)
    transcript = transcribe_audio(tmp_path) if ext in AUDIO_EXTENSIONS else transcribe_video(tmp_path)

    resource = models.Resource(topic_id=topic_id, type="video", title=filename, transcript=transcript, status="ready")
    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, transcript)
    return resource
