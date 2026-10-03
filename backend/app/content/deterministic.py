"""Publish deterministic content as-is.

Every topic has two kinds of material:

- Deterministic: shipped with the app and sourced verbatim (or hand-written
  from a cited source) -- each official event's rules overview, the seeded
  scioly.org wiki excerpts, the 2027-rules study notes, and the Solar
  System source-reader chapters (flashcards, story, infographics). It
  never needs an LLM, so it goes
  straight to students: every student can see it, no coach clicks and no
  roster assignment.
- Generative: whatever a coach chooses to add with the AI tools (draft
  flashcards, stories, illustrations). Optional, reviewed and published by
  the coach as before -- and it can now read the deterministic sources too
  (see explain.ensure_deterministic_sources_indexed).

This runs on every startup after all seeds. It is idempotent, and the
"publish" step only fires the first time a chapter is marked open, so a
coach who later unpublishes a chapter is never overridden.
"""

from app import models
from app.db import SessionLocal

# Titles of the resources the startup seeds create from cited sources.
DETERMINISTIC_TITLE_PREFIXES = ("scioly.org wiki:", "Source reader:", "Study notes:")


def publish_deterministic_content() -> None:
    db = SessionLocal()
    try:
        for resource in db.query(models.Resource).filter(models.Resource.type == "text"):
            if not resource.deterministic and resource.title.startswith(DETERMINISTIC_TITLE_PREFIXES):
                resource.deterministic = True
        db.flush()

        # Official events: the ones carrying the seeded rules overview
        # (coach-created custom topics never get one). Their rules and
        # source notes are visible to every student.
        events = (
            db.query(models.Topic)
            .filter(models.Topic.parent_topic_id.is_(None), models.Topic.overview_what != "")
            .all()
        )
        for event in events:
            event.open_to_all_students = True

        # Sourced chapters: any sub-topic holding deterministic material.
        # Published the first time it's opened up; after that the coach's
        # publish toggle is left alone.
        chapter_ids = {
            row[0]
            for row in db.query(models.Resource.topic_id).filter(models.Resource.deterministic.is_(True))
        }
        if chapter_ids:
            chapters = (
                db.query(models.Topic)
                .filter(models.Topic.id.in_(chapter_ids), models.Topic.parent_topic_id.isnot(None))
                .all()
            )
            for chapter in chapters:
                if not chapter.open_to_all_students:
                    chapter.open_to_all_students = True
                    chapter.content_published = True

        db.commit()
    finally:
        db.close()
