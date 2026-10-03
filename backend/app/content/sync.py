"""Keep seeded study material in step with the code that ships it.

The per-event seeds in main.py used to insert a resource or chapter only if
it was missing, so editing its text in code never reached a database that
had already been seeded. These helpers create-or-update instead: when the
shipped text changes, the stored row is rewritten and, if it had already
been embedded for AI generation, its old vector chunks are dropped so the
next generation run re-indexes the new text (see
explain.ensure_deterministic_sources_indexed).

Rows are matched by title/name, with `old_titles`/`old_names` covering a
rename, so a renamed chapter is updated in place rather than duplicated.
"""

import logging

from sqlalchemy.orm import Session

from app import models

logger = logging.getLogger(__name__)


def sync_resource(
    db: Session,
    topic_id: int,
    title: str,
    source_url: str,
    raw_text: str,
    old_titles: tuple[str, ...] = (),
) -> models.Resource:
    resource = (
        db.query(models.Resource)
        .filter(models.Resource.topic_id == topic_id, models.Resource.title.in_((title, *old_titles)))
        .order_by(models.Resource.id)
        .first()
    )
    if resource is None:
        resource = models.Resource(topic_id=topic_id, type="text", title=title, source_url=source_url, raw_text=raw_text)
        db.add(resource)
        db.flush()
        return resource

    if resource.raw_text != raw_text and resource.chunks_indexed:
        try:
            from app.rag.vectorstore import delete_resource

            delete_resource(resource.id)
        except Exception:  # vector store unavailable -- re-indexing still happens below
            logger.exception("Could not drop stale chunks for resource %s", resource.id)
        resource.chunks_indexed = False
    resource.title = title
    resource.source_url = source_url
    resource.raw_text = raw_text
    return resource


def sync_chapter(
    db: Session,
    event: models.Topic,
    name: str,
    description: str,
    resource_title: str,
    source_url: str,
    text: str,
    old_names: tuple[str, ...] = (),
    old_resource_titles: tuple[str, ...] = (),
) -> models.Topic:
    chapter = (
        db.query(models.Topic)
        .filter(models.Topic.parent_topic_id == event.id, models.Topic.name.in_((name, *old_names)))
        .order_by(models.Topic.id)
        .first()
    )
    if chapter is None:
        chapter = models.Topic(
            event_name=event.event_name,
            name=name,
            description=description,
            assessment_type=event.assessment_type,
            parent_topic_id=event.id,
        )
        db.add(chapter)
        db.flush()
    else:
        chapter.name = name
        chapter.description = description
    sync_resource(db, chapter.id, resource_title, source_url, text, old_resource_titles)
    return chapter
