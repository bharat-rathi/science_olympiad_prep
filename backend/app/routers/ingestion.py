import base64
import shutil
import tempfile
import zipfile
from pathlib import Path
from urllib.parse import urlparse

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, UploadFile
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import SessionLocal, get_db
from app.rag.chunking import chunk_text
from app.rag.drive_fetch import fetch_drive_video, get_drive_video_info, is_drive_url
from app.rag.embeddings import embed_texts
from app.rag.link_fetch import fetch_url_text
from app.rag.pdf_extract import extract_pdf_text
from app.rag.transcription import stream_upload_to_temp, transcribe_audio, transcribe_video
from app.rag.vectorstore import add_chunks, delete_resource as delete_resource_chunks
from app.rag.web_research import research_topic
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


def _fail_resource(db: Session, resource: models.Resource, error: Exception) -> None:
    resource.status = "failed"
    resource.error_message = str(error) if isinstance(error, ValueError) else (
        "Something went wrong processing this video -- try again."
    )
    db.commit()


def _process_drive_video(resource_id: int, url: str, coach_id: int) -> None:
    """Background task: download + transcribe a Drive video and finish
    setting up its Resource row.

    Uses its own fresh DB session -- never the request's, which is long
    closed by the time this runs regardless. This is the whole point of
    moving this off the request/response cycle: a Drive video can take
    10+ minutes to download and transcribe, and holding the request's
    session open (idle, doing nothing DB-related) for that long against
    Neon's serverless Postgres reliably triggered a PendingRollbackError
    once the connection got closed server-side for being idle too long.
    """
    db = SessionLocal()
    try:
        resource = db.get(models.Resource, resource_id)
        if not resource:
            return  # deleted before processing started
        try:
            coach = db.get(models.Coach, coach_id)
            title, text = fetch_drive_video(url, coach)
            resource.title = title
            resource.transcript = text
            resource.status = "ready"
            db.commit()
            _index_resource(db, resource, text)
        except Exception as e:
            _fail_resource(db, resource, e)
    finally:
        db.close()


def _process_uploaded_media(resource_id: int, tmp_path_str: str, ext: str) -> None:
    """Background task: transcribe an already-saved video/audio file and
    finish setting up its Resource row. Same rationale as
    _process_drive_video above -- transcription can take a while, so it
    can't happen on the request's DB session.
    """
    tmp_path = Path(tmp_path_str)
    db = SessionLocal()
    try:
        resource = db.get(models.Resource, resource_id)
        if not resource:
            return
        try:
            text = transcribe_audio(tmp_path) if ext in AUDIO_EXTENSIONS else transcribe_video(tmp_path)
            resource.transcript = text
            resource.status = "ready"
            db.commit()
            _index_resource(db, resource, text)
        except Exception as e:
            _fail_resource(db, resource, e)
    finally:
        db.close()
        tmp_path.unlink(missing_ok=True)


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


def _looks_like_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in ("http", "https") and bool(parsed.hostname)


@router.post("/{topic_id}/resources/link", response_model=schemas.ResourceOut)
def add_link_resource(
    topic_id: int,
    payload: schemas.ResourceCreateLink,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Fetch a real URL and ingest its content -- no copy/paste required.

    Google Drive video links are downloaded and transcribed via Gemini
    (requires the coach to have connected Drive in Settings first); YouTube
    links are detected and routed to the official captions track (no LLM,
    no video download); other http(s) URLs go through the generic
    readable-content extractor. If the coach didn't paste a URL at all --
    just typed a keyword or topic name -- this falls back to the research
    agent (rag/web_research.py), which searches the web and synthesizes
    findings instead. Either way the result lands in the same resource pool
    for concept generation to draw from.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    value = payload.url.strip()

    if is_drive_url(value):
        # Drive videos can take 10+ minutes to download and transcribe --
        # only the fast metadata/validation check happens here, synchronously,
        # for instant feedback on bad input; the actual work runs as a
        # background task (see _process_drive_video) so this request can
        # return immediately instead of holding the DB session open for the
        # whole thing (see that function's docstring for why that matters).
        try:
            info = get_drive_video_info(value, coach)
        except ValueError as e:
            raise HTTPException(422, str(e))
        resource = models.Resource(
            topic_id=topic_id, type="video", title=info["title"], source_url=value, status="pending"
        )
        db.add(resource)
        db.commit()
        db.refresh(resource)
        background_tasks.add_task(_process_drive_video, resource.id, value, coach.id)
        return resource

    try:
        if is_youtube_url(value):
            resource_type = "video"
            title, text = fetch_youtube_transcript(value)
        elif _looks_like_url(value):
            resource_type = "link"
            title, text = fetch_url_text(value)
        else:
            resource_type = "research"
            found = research_topic(value, topic.name, topic.description, coach)
            title = found["title"]
            text = found["text"]
            if found["sources"]:
                text += "\n\nSources:\n" + "\n".join(f"- {s['title']} -- {s['url']}" for s in found["sources"])
    except ValueError as e:
        raise HTTPException(422, str(e))

    resource = models.Resource(
        topic_id=topic_id,
        type=resource_type,
        title=title,
        source_url=value if resource_type != "research" else "",
        raw_text=text if resource_type in ("link", "research") else "",
        transcript=text if resource_type == "video" else "",
        status="ready",
    )
    db.add(resource)
    db.commit()
    db.refresh(resource)

    _index_resource(db, resource, text)
    return resource


@router.delete("/{topic_id}/resources/{resource_id}", status_code=204)
def delete_resource(
    topic_id: int,
    resource_id: int,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    resource = db.get(models.Resource, resource_id)
    if not resource or resource.topic_id != topic_id:
        raise HTTPException(404, "Resource not found")
    db.delete(resource)
    db.commit()
    # Concepts already generated from this resource keep their explanations --
    # only the source material and its indexed chunks go away, so a coach
    # removing a bad upload doesn't silently wipe content students already see.
    delete_resource_chunks(resource_id)


SUPPORTED_UPLOAD_EXTENSIONS = VIDEO_EXTENSIONS | AUDIO_EXTENSIONS | PDF_EXTENSIONS


@router.post("/{topic_id}/resources/upload", response_model=list[schemas.ResourceOut])
async def upload_media_resource(
    topic_id: int,
    file: UploadFile,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    coach: models.Coach = Depends(auth.require_coach),
):
    """Upload a video/audio/PDF file, or a zip of several, for ingestion.

    PDFs go through plain text extraction (no LLM) synchronously, same as
    always. Video/audio go through Gemini transcription -- which can take
    a long time for a longer file -- as a background task (see
    _process_uploaded_media): this endpoint creates a "pending" Resource
    and returns immediately rather than holding the request (and its DB
    session) open for however long transcription takes. A zip is unpacked
    and each supported file inside it is processed the same way, per-file.

    Streams straight to disk (stream_upload_to_temp / zf.extract) rather than
    ever holding the whole upload in memory as one bytes object -- a
    resource PDF full of high-res diagrams/photos can easily be 50-100MB,
    and this app runs on a memory-constrained host.
    """
    topic = db.get(models.Topic, topic_id)
    if not topic:
        raise HTTPException(404, "Topic not found")

    filename = file.filename or "upload"
    suffix = Path(filename).suffix.lower()

    created: list[models.Resource] = []
    try:
        if suffix == ".zip":
            tmp_zip = stream_upload_to_temp(file.file, filename)
            try:
                with zipfile.ZipFile(tmp_zip) as zf, tempfile.TemporaryDirectory() as extract_dir:
                    for name in zf.namelist():
                        ext = Path(name).suffix.lower()
                        if ext not in SUPPORTED_UPLOAD_EXTENSIONS:
                            continue
                        extracted_path = Path(zf.extract(name, path=extract_dir))
                        if ext not in PDF_EXTENSIONS:
                            # extract_dir is deleted when this `with` block
                            # exits -- well before a background task would
                            # run -- so a video/audio file needs a durable
                            # copy outside it first.
                            extracted_path = _persist_temp_copy(extracted_path)
                        created.append(
                            _ingest_from_path(db, background_tasks, topic_id, Path(name).name, extracted_path, ext, coach)
                        )
            finally:
                tmp_zip.unlink(missing_ok=True)
        elif suffix in SUPPORTED_UPLOAD_EXTENSIONS:
            tmp_path = stream_upload_to_temp(file.file, filename)
            created.append(_ingest_from_path(db, background_tasks, topic_id, filename, tmp_path, suffix, coach))
        else:
            raise HTTPException(400, f"Unsupported file type: {suffix}")
    except ValueError as e:
        raise HTTPException(422, str(e))

    return created


def _persist_temp_copy(path: Path) -> Path:
    """Copy a file to a new standalone temp file that will survive past
    this request -- used for a video/audio file extracted from a zip into
    a TemporaryDirectory that gets deleted as soon as that `with` block
    exits, before a background task handed the path would get a chance to
    read it.
    """
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=path.suffix)
    try:
        with open(path, "rb") as src:
            shutil.copyfileobj(src, tmp)
    finally:
        tmp.close()
    return Path(tmp.name)


def _ingest_from_path(
    db: Session, background_tasks: BackgroundTasks, topic_id: int, filename: str, tmp_path: Path, ext: str,
    coach: models.Coach | None = None,
) -> models.Resource:
    if ext in PDF_EXTENSIONS:
        try:
            text, diagram_data = extract_pdf_text(tmp_path, coach)
        finally:
            tmp_path.unlink(missing_ok=True)

        resource = models.Resource(topic_id=topic_id, type="pdf", title=filename, raw_text=text, status="ready")
        db.add(resource)
        db.commit()
        db.refresh(resource)

        for d in diagram_data:
            db.add(
                models.Diagram(
                    topic_id=topic_id,
                    resource_id=resource.id,
                    image_data_url="data:image/jpeg;base64," + base64.b64encode(d["image_bytes"]).decode("ascii"),
                    caption=d["caption"],
                    page_number=d["page_number"],
                )
            )
        if diagram_data:
            db.commit()

        _index_resource(db, resource, text)
        return resource

    # Video/audio: transcription can take a long time (Gemini has to
    # process the whole file), so it's handed off to a background task
    # instead of blocking this request -- see _process_uploaded_media.
    # That task owns tmp_path from here on, including deleting it when done.
    resource = models.Resource(topic_id=topic_id, type="video", title=filename, status="pending")
    db.add(resource)
    db.commit()
    db.refresh(resource)
    background_tasks.add_task(_process_uploaded_media, resource.id, str(tmp_path), ext)
    return resource
