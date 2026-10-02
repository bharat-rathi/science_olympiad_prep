"""Deterministic seed for the Solar System learning chapters.

Turns the hand-written chapters (chapters_a/b/c.py) and the SVG
infographics into ordinary rows -- a sub-topic per chapter under the
"Solar System" event, a fact-sheet Resource, approved ConceptTerm
flashcards with badge images, the long-form story, and infographic
Diagrams -- publishes them, and marks them open_to_all_students, so every
student gets real learning material with no LLM call, no coach clicks and
no roster assignment.

Runs on every startup and keeps existing databases in step with this file:
sourced content (origin "sourced", story_origin "sourced", the seeded fact
sheet and infographics) is updated to the latest text and images, and
sourced cards that were merged away are removed. Anything a coach touched is
left alone: an edited card becomes origin "coach" (topics.update_concept),
a rewritten story becomes "coach"/"ai", AI drafts are origin "ai", and a
coach's unpublish is never undone.

It also retires the four older wiki-excerpt chapters whose content was
merged into these (see retire_legacy_chapters).
"""

import logging

from app import models
from app.content.solar_system.chapters_a import CHAPTERS_A
from app.content.solar_system.chapters_b import CHAPTERS_B
from app.content.solar_system.chapters_c import CHAPTERS_C
from app.content.solar_system.infographics import INFOGRAPHICS
from app.content.solar_system.svg import badge_svg, data_url
from app.db import SessionLocal

log = logging.getLogger(__name__)

CHAPTERS = CHAPTERS_A + CHAPTERS_B + CHAPTERS_C
SOURCE_URL = "https://openstax.org/details/books/astronomy-2e"

# Chapters the older wiki seed (main.py's seed_solar_system_deep_dive) used
# to create. Their content now lives in CHAPTERS, mostly chapters_c.py.
LEGACY_CHAPTER_NAMES = (
    "Solar System: Star & Planet Formation",
    "Solar System: Bodies, Moons & Small Bodies",
    "Solar System: Habitability & Exoplanet Types",
    "Solar System: Orbital Mechanics, Eclipses & History",
)
LEGACY_RESOURCE_TITLE = "scioly.org wiki: Solar System (excerpt for this chapter)"

# Card terms earlier versions of this seed created that were since merged
# into other cards -- still recognized as sourced so the sync can remove them.
RETIRED_TERMS = {
    "Circumstellar (protoplanetary) disks",
    "Dwarf planets and TNOs",
    "Asteroids, comets and dust",
    "Exploring by spacecraft",
    "Carl Sagan",
    "Photosynthesis and the rise of oxygen",
    "Life removed Earth's CO2",
    "How life changed Earth's air",
    "Titan's nitrogen atmosphere",
    "Photosynthesis and the oxygen revolution",
    "Inflated hot Jupiters and cold Jupiters",
    "Did our planets move?",
}


def retire_legacy_chapters(db, parent: models.Topic) -> None:
    """Delete a legacy chapter if it still holds only its seeded excerpt.
    If a coach built anything on it (concepts, an assessment, a schedule
    entry, extra resources, sub-chapters), keep it for the coach but hide it
    from students so the event shows one de-duplicated set of chapters."""
    legacy = (
        db.query(models.Topic)
        .filter(models.Topic.parent_topic_id == parent.id, models.Topic.name.in_(LEGACY_CHAPTER_NAMES))
        .all()
    )
    for chapter in legacy:
        coach_work = (
            db.query(models.ConceptTerm).filter_by(topic_id=chapter.id).count()
            + db.query(models.Assessment).filter_by(topic_id=chapter.id).count()
            + db.query(models.ScheduleEntry).filter_by(topic_id=chapter.id).count()
            + db.query(models.Topic).filter_by(parent_topic_id=chapter.id).count()
            + db.query(models.Resource)
            .filter(models.Resource.topic_id == chapter.id, models.Resource.title != LEGACY_RESOURCE_TITLE)
            .count()
        )
        if coach_work:
            chapter.open_to_all_students = False
            chapter.content_published = False
            # Retire its excerpt too, so app/content/deterministic.py doesn't
            # see sourced material here and publish the chapter again.
            for resource in chapter.resources:
                if resource.title == LEGACY_RESOURCE_TITLE:
                    resource.title = "Retired (merged into the Solar System chapters): " + resource.title
                    resource.deterministic = False
            continue
        for resource in chapter.resources:
            if resource.chunks_indexed:
                try:
                    from app.rag.vectorstore import delete_resource

                    delete_resource(resource.id)
                except Exception:  # vector store unavailable -- orphaned chunks are harmless
                    log.warning("Could not delete indexed chunks for resource %s", resource.id)
        db.query(models.StudentTopic).filter_by(topic_id=chapter.id).delete()
        db.query(models.Diagram).filter_by(topic_id=chapter.id).delete()
        db.delete(chapter)
    db.flush()


def _sync_chapter(db, parent: models.Topic, chapter: dict) -> None:
    chapter_topic = (
        db.query(models.Topic)
        .filter(models.Topic.name == chapter["name"], models.Topic.parent_topic_id == parent.id)
        .first()
    )
    if chapter_topic is None:
        chapter_topic = models.Topic(
            event_name=parent.event_name,
            name=chapter["name"],
            description=chapter["description"],
            assessment_type=parent.assessment_type,
            parent_topic_id=parent.id,
            story_md=chapter["story"],
            story_origin="sourced",
            content_published=True,
            open_to_all_students=True,
        )
        db.add(chapter_topic)
        db.flush()
    else:
        if not chapter_topic.open_to_all_students:
            # Backfill for chapters created before this flag existed. A coach
            # hides a chapter by unpublishing, which this never undoes.
            chapter_topic.open_to_all_students = True
        chapter_topic.description = chapter["description"]
        if chapter_topic.story_origin == "sourced" or not chapter_topic.story_md:
            chapter_topic.story_md = chapter["story"]
            chapter_topic.story_origin = "sourced"

    # Seeded fact sheet, matched by title -- or by the seeded prefix so a
    # retitled sheet is updated in place rather than duplicated.
    resource = (
        db.query(models.Resource)
        .filter(models.Resource.topic_id == chapter_topic.id, models.Resource.title == chapter["source_title"])
        .first()
    ) or (
        db.query(models.Resource)
        .filter(
            models.Resource.topic_id == chapter_topic.id,
            models.Resource.deterministic.is_(True),
            models.Resource.title.startswith("Source reader:") | models.Resource.title.startswith("Source notes:"),
        )
        .first()
    )
    if resource is None:
        resource = models.Resource(
            topic_id=chapter_topic.id,
            type="text",
            title=chapter["source_title"],
            source_url=SOURCE_URL,
            raw_text=chapter["source_text"],
            deterministic=True,
        )
        db.add(resource)
        db.flush()
    elif resource.raw_text != chapter["source_text"] or resource.title != chapter["source_title"]:
        resource.title = chapter["source_title"]
        resource.raw_text = chapter["source_text"]
        resource.deterministic = True
        resource.chunks_indexed = False  # re-index on the next AI run

    # Infographics: refresh images in place, add new ones, drop merged-away ones.
    wanted = {INFOGRAPHICS[key][0]: (page, INFOGRAPHICS[key][1]) for page, key in enumerate(chapter["infographics"], start=1)}
    existing_diagrams = db.query(models.Diagram).filter(models.Diagram.resource_id == resource.id).all()
    for diagram in existing_diagrams:
        if diagram.caption not in wanted:
            db.delete(diagram)
    have = {d.caption: d for d in existing_diagrams}
    for caption, (page, build) in wanted.items():
        image = data_url(build())
        if caption in have:
            have[caption].image_data_url = image
            have[caption].page_number = page
        else:
            db.add(
                models.Diagram(
                    topic_id=chapter_topic.id, resource_id=resource.id, image_data_url=image, caption=caption, page_number=page
                )
            )

    # Flashcards: sync sourced cards, add new ones, and remove sourced ones
    # that were merged into another card. Coach-edited ("coach") and AI
    # ("ai") cards are never touched.
    seeded = {concept["term"]: concept for concept in chapter["concepts"]}
    existing = db.query(models.ConceptTerm).filter(models.ConceptTerm.topic_id == chapter_topic.id).all()
    existing_terms = set()
    for row in existing:
        existing_terms.add(row.term)
        if (
            row.origin == "ai"
            and row.approved
            and row.source_resource_ids == [resource.id]
            and (row.term in seeded or row.term in RETIRED_TERMS)
        ):
            row.origin = "sourced"  # backfill: created by this seed before `origin` existed
        if row.origin != "sourced":
            continue
        concept = seeded.get(row.term)
        if concept is None:
            db.delete(row)
            continue
        label, sub, color = concept["badge"]
        row.explanation_md = concept["explanation"]
        row.analogy = concept["analogy"]
        row.why_it_matters = concept["why"]
        row.source_resource_ids = [resource.id]
        row.image_data_url = data_url(badge_svg(label, sub, color))
    for term, concept in seeded.items():
        if term in existing_terms:
            continue
        label, sub, color = concept["badge"]
        db.add(
            models.ConceptTerm(
                topic_id=chapter_topic.id,
                term=term,
                explanation_md=concept["explanation"],
                analogy=concept["analogy"],
                why_it_matters=concept["why"],
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
        retire_legacy_chapters(db, parent)
        for chapter in CHAPTERS:
            _sync_chapter(db, parent, chapter)
        db.commit()
    finally:
        db.close()
