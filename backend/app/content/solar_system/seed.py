"""Deterministic seed for the Solar System study material.

The event's material is a structured study plan (plan.py) of 19 lesson
chapters (lessons_unit1..6.py), built from the coach-supplied source reader
and scioly.org wiki with duplicates removed. Each chapter becomes a
sub-topic of the "Solar System" event with:

- lesson_json: the in-depth lesson (sections with inline infographics, a
  word bank explaining every jargon word, note-sheet facts, quick-check
  questions) that the student page renders;
- approved, origin "sourced" ConceptTerm flashcards with badge images;
- infographic Diagrams (deterministic SVGs) hung off one "Lesson notes"
  Resource, which also holds the full lesson text for the AI tools;
- story_md: the same lesson as plain text (presentation / coach view).

Everything is published and open to every student -- no LLM call, no coach
click, no roster assignment. The event row itself gets the study plan as
its lesson_json; its rules overview (overview_*) is never touched here.

CONTENT REBUILD: the first startup with this version wipes all earlier
Solar System study material (older chapters, their flashcards, diagrams,
resources and stories, plus anything on the event row except the rules) so
students see one clean, deduplicated set. AppMeta records the version, so
the wipe never repeats and later coach work is safe. A chapter that holds a
coach's assessment is not deleted -- its study material is removed and it
is hidden and renamed "Archived: ...", keeping the tests and attempts.

After that, every startup syncs the shipped content: sourced cards, the
sourced story, the lesson and the infographics are updated; cards a coach
edited (origin "coach") or AI drafts (origin "ai") are left alone, and a
coach's unpublish is never undone.
"""

import logging

from app import models
from app.content.solar_system.infographics import INFOGRAPHICS
from app.content.solar_system.plan import CHAPTERS, UNITS, plan_json
from app.content.solar_system.svg import badge_svg, data_url
from app.db import SessionLocal

log = logging.getLogger(__name__)

CONTENT_KEY = "solar_system_content_version"
CONTENT_VERSION = "lessons-v1"
SOURCE_URL = "https://scioly.org/wiki/Solar_System"
ARCHIVED_PREFIX = "Archived: "
UNIT_TITLES = {unit["number"]: unit["title"] for unit in UNITS}


# ---------------------------------------------------------------- the wipe


def _drop_indexed(resource: models.Resource) -> None:
    if not resource.chunks_indexed:
        return
    try:
        from app.rag.vectorstore import delete_resource

        delete_resource(resource.id)
    except Exception:  # vector store unavailable -- orphaned chunks are harmless
        log.warning("Could not delete indexed chunks for resource %s", resource.id)


def _strip_study_material(db, topic: models.Topic) -> None:
    """Remove a topic's learning material (flashcards, diagrams, resources,
    story, lesson) but leave its rules, assessments and chat history."""
    for resource in topic.resources:
        _drop_indexed(resource)
    resource_ids = [r.id for r in topic.resources]
    db.query(models.Diagram).filter(
        (models.Diagram.topic_id == topic.id) | models.Diagram.resource_id.in_(resource_ids)
    ).delete(synchronize_session=False)
    db.query(models.Resource).filter_by(topic_id=topic.id).delete(synchronize_session=False)
    db.query(models.ConceptTerm).filter_by(topic_id=topic.id).delete(synchronize_session=False)
    db.expire(topic, ["resources", "concepts"])
    topic.story_md = ""
    topic.story_origin = ""
    topic.lesson_json = None


def _wipe_chapter(db, chapter: models.Topic) -> None:
    for child in db.query(models.Topic).filter_by(parent_topic_id=chapter.id).all():
        _wipe_chapter(db, child)
    _strip_study_material(db, chapter)
    if db.query(models.Assessment).filter_by(topic_id=chapter.id).count():
        # Keep the coach's tests (and students' attempts) -- hide the rest.
        chapter.content_published = False
        chapter.open_to_all_students = False
        if not chapter.name.startswith(ARCHIVED_PREFIX):
            chapter.name = (ARCHIVED_PREFIX + chapter.name)[:200]
        return
    db.query(models.StudentTopic).filter_by(topic_id=chapter.id).delete()
    db.query(models.ScheduleEntry).filter_by(topic_id=chapter.id).delete()
    db.query(models.TopicChatMessage).filter_by(topic_id=chapter.id).delete()
    db.flush()
    db.delete(chapter)


def wipe_old_study_material(db, parent: models.Topic) -> None:
    """One-time clean slate: every Solar System chapter and every piece of
    study material on the event row goes, except the rules overview."""
    for chapter in db.query(models.Topic).filter_by(parent_topic_id=parent.id).all():
        _wipe_chapter(db, chapter)
    _strip_study_material(db, parent)
    db.flush()


# ---------------------------------------------------------------- the sync


def lesson_text(chapter: dict) -> str:
    """The whole chapter as plain text: the story_md view, the Lesson notes
    resource the AI tools read, and what the Ask box searches."""
    parts = [chapter["name"].removeprefix("Solar System: ").upper(), chapter["description"], ""]
    parts.append("BY THE END OF THIS CHAPTER YOU CAN:")
    parts += [f"• {goal}" for goal in chapter["goals"]]
    for section in chapter["sections"]:
        parts += ["", section["heading"].upper(), "", section["body"]]
    parts += ["", "WORD BANK"]
    parts += [f"• {word}: {meaning}" for word, meaning in chapter["word_bank"]]
    parts += ["", "NOTE-SHEET FACTS"]
    parts += [f"• {fact}" for fact in chapter["key_facts"]]
    parts += ["", "QUICK CHECK"]
    for question, answer in chapter["quick_check"]:
        parts += [f"Q: {question}", f"A: {answer}"]
    return "\n".join(parts)


def lesson_json(chapter: dict) -> dict:
    return {
        "kind": "lesson",
        "unit": chapter["unit"],
        "unit_title": UNIT_TITLES[chapter["unit"]],
        "goals": chapter["goals"],
        "sections": [
            {
                "heading": section["heading"],
                "body": section["body"],
                "infographic": INFOGRAPHICS[section["infographic"]][0] if section.get("infographic") else None,
            }
            for section in chapter["sections"]
        ],
        "word_bank": [{"word": word, "meaning": meaning} for word, meaning in chapter["word_bank"]],
        "key_facts": chapter["key_facts"],
        "quick_check": [{"q": q, "a": a} for q, a in chapter["quick_check"]],
    }


def _resource_title(chapter: dict) -> str:
    return "Lesson notes: " + chapter["name"].removeprefix("Solar System: ")


def _sync_chapter(db, parent: models.Topic, chapter: dict) -> None:
    text_version = lesson_text(chapter)
    topic = (
        db.query(models.Topic)
        .filter(models.Topic.name == chapter["name"], models.Topic.parent_topic_id == parent.id)
        .first()
    )
    if topic is None:
        topic = models.Topic(
            event_name=parent.event_name,
            name=chapter["name"],
            description=chapter["description"],
            assessment_type=parent.assessment_type,
            parent_topic_id=parent.id,
            story_md=text_version,
            story_origin="sourced",
            content_published=True,
            open_to_all_students=True,
        )
        db.add(topic)
        db.flush()
    else:
        topic.open_to_all_students = True  # a coach hides a chapter by unpublishing
        topic.description = chapter["description"]
        if topic.story_origin in ("sourced", ""):
            topic.story_md = text_version
            topic.story_origin = "sourced"
    topic.lesson_json = lesson_json(chapter)

    # One deterministic "Lesson notes" resource per chapter: the full text for
    # the AI tools, and the owner of the chapter's infographics.
    resource = (
        db.query(models.Resource)
        .filter(models.Resource.topic_id == topic.id, models.Resource.title.startswith("Lesson notes:"))
        .first()
    )
    if resource is None:
        resource = models.Resource(
            topic_id=topic.id,
            type="text",
            title=_resource_title(chapter),
            source_url=SOURCE_URL,
            raw_text=text_version,
            deterministic=True,
        )
        db.add(resource)
        db.flush()
    elif resource.raw_text != text_version or resource.title != _resource_title(chapter):
        resource.title = _resource_title(chapter)
        resource.raw_text = text_version
        resource.deterministic = True
        resource.chunks_indexed = False  # re-index on the next AI run

    # Infographics, in reading order.
    keys = [s["infographic"] for s in chapter["sections"] if s.get("infographic")]
    wanted = {INFOGRAPHICS[key][0]: (page, INFOGRAPHICS[key][1]) for page, key in enumerate(keys, start=1)}
    existing = db.query(models.Diagram).filter(models.Diagram.resource_id == resource.id).all()
    for diagram in existing:
        if diagram.caption not in wanted:
            db.delete(diagram)
    have = {d.caption: d for d in existing}
    for caption, (page, build) in wanted.items():
        image = data_url(build())
        if caption in have:
            have[caption].image_data_url = image
            have[caption].page_number = page
        else:
            db.add(models.Diagram(topic_id=topic.id, resource_id=resource.id, image_data_url=image, caption=caption, page_number=page))

    # Flashcards: sourced cards follow this file; coach/AI cards are untouched.
    seeded = {card["term"]: card for card in chapter["cards"]}
    existing_terms = set()
    for row in db.query(models.ConceptTerm).filter(models.ConceptTerm.topic_id == topic.id).all():
        existing_terms.add(row.term)
        if row.origin != "sourced":
            continue
        card = seeded.get(row.term)
        if card is None:
            db.delete(row)
            continue
        label, sub, color = card["badge"]
        row.explanation_md = card["explanation"]
        row.analogy = card["analogy"]
        row.why_it_matters = card["why"]
        row.source_resource_ids = [resource.id]
        row.image_data_url = data_url(badge_svg(label, sub, color))
    for term, card in seeded.items():
        if term in existing_terms:
            continue
        label, sub, color = card["badge"]
        db.add(
            models.ConceptTerm(
                topic_id=topic.id,
                term=term,
                explanation_md=card["explanation"],
                analogy=card["analogy"],
                why_it_matters=card["why"],
                source_resource_ids=[resource.id],
                approved=True,
                origin="sourced",
                image_data_url=data_url(badge_svg(label, sub, color)),
            )
        )


def seed_solar_system_learning_content() -> None:
    db = SessionLocal()
    try:
        parent = (
            db.query(models.Topic)
            .filter(models.Topic.name == "Solar System", models.Topic.parent_topic_id.is_(None))
            .first()
        )
        if parent is None:
            return
        meta = db.get(models.AppMeta, CONTENT_KEY)
        if meta is None or meta.value != CONTENT_VERSION:
            wipe_old_study_material(db, parent)
            if meta is None:
                meta = models.AppMeta(key=CONTENT_KEY)
                db.add(meta)
            meta.value = CONTENT_VERSION
        parent.lesson_json = plan_json()
        for chapter in CHAPTERS:
            _sync_chapter(db, parent, chapter)
        db.commit()
    finally:
        db.close()
