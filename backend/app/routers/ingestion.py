import zipfile
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db
from app.rag.chunking import chunk_text
from app.rag.embeddings import embed_texts
from app.rag.link_fetch import fetch_url_text
from app.rag.pdf_extract import extract_pdf_text
from app.rag.transcription import save_upload_to_temp, transcribe_audio, transcribe_video
from app.rag.vectorstore import add_chunks
from app.rag.youtube_fetch import fetch_youtube_transcript, is_youtube_url

router = APIRouter(prefix="/api/topics", tags=["ingestion"])

VIDEO_EXTENSIONS = {".mp4", ".mov", ".mkv", ".avi", ".webm"}
AUDIO_EXTENSIONS = {".mp3", ".wav", ".m4a", ".flac"}
PDF_EXTENSIONS = {".pdf"}


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
def add_text_resource(
    topic_id: int,
    payload: schemas.ResourceCreateText,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
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
def add_link_resource(
    topic_id: int,
    payload: schemas.ResourceCreateLink,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Fetch a real URL and ingest its content -- no copy/paste required.

    YouTube links are detected and routed to the official captions track
    (no LLM, no video download); everything else goes through the generic
    readable-content extractor.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    try:
        if is_youtube_url(payload.url):
            resource_type = "video"
            title, text = fetch_youtube_transcript(payload.url)
        else:
            resource_type = "link"
            title, text = fetch_url_text(payload.url)
    except ValueError as e:
        raise HTTPException(422, str(e))

    resource = models.Resource(
        topic_id=topic_id,
        type=resource_type,
        title=title,
        source_url=payload.url,
        raw_text=text if resource_type == "link" else "",
        transcript=text if resource_type == "video" else "",
        status="ready",
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, text)
    return resource


SUPPORTED_UPLOAD_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS | PDF_EXTENSIONS


@router.post("/{topic_id}/resources/upload", response_model=list[schemas.ResourceOut])
async def upload_media_resource(
    topic_id: int,
    file: UploadFile,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Upload a video/audio/PDF file, or a zip of several, for ingestion.

    Video/audio go through Gemini transcription; PDFs go through plain text
    extraction (no LLM). A zip is unpacked and each supported file inside it
    is processed the same way.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    data = await file.read()
    filename = file.filename or "upload"
    suffix = Path(filename).suffix.lower()

    created: list[models.Resource] = []
    try:
        if suffix == ".zip":
            tmp_zip = save_upload_to_temp(filename, data)
            with zipfile.ZipFile(tmp_zip) as zf:
                for name in zf.namelist():
                    ext = Path(name).suffix.lower()
                    if ext not in SUPPORTED_UPLOAD_EXTENSIONS:
                        continue
                    with zf.open(name) as member:
                        member_bytes = member.read()
                    created.append(_ingest_upload_and_create(db, topic_id, name, member_bytes, ext))
        elif suffix in SUPPORTED_UPLOAD_EXTENSIONS:
            created.append(_ingest_upload_and_create(db, topic_id, filename, data, suffix))
        else:
            raise HTTPException(400, f"Unsupported file type: {suffix}")
    except ValueError as e:
        raise HTTPException(422, str(e))

    return created


def _ingest_upload_and_create(db: Session, topic_id: int, filename: str, data: bytes, ext: str) -> models.Resource:
    tmp_path = save_upload_to_temp(filename, data)

    if ext in PDF_EXTENSIONS:
        text = extract_pdf_text(tmp_path)
        resource = models.Resource(topic_id=topic_id, type="pdf", title=filename, raw_text=text, status="ready")
    else:
        text = transcribe_audio(tmp_path) if ext in AUDIO_EXTENSIONS else transcribe_video(tmp_path)
        resource = models.Resource(topic_id=topic_id, type="video", title=filename, transcript=text, status="ready")

    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, text)
    return resource
