"""Deterministic seed for the Solar System learning chapters.

Turns the hand-written chapters (chapters_a.py / chapters_b.py) and the SVG
infographics into ordinary rows -- a sub-topic per chapter under the
"Solar System" event, a fact-sheet Resource, approved ConceptTerm
flashcards with badge images, the long-form story, and infographic
Diagrams -- publishes them, and marks them open_to_all_students, so every
student gets real learning material with no LLM call, no coach clicks and
no roster assignment.

Idempotent and non-destructive, like the other startup seeds in main.py:
every row is matched by name/title/term/caption and only created when
missing, so re-running on each startup never duplicates anything and never
overwrites a coach's later edits (an edited flashcard, a rewritten story,
an unpublished chapter).
"""

from app import models
from app.content.solar_system.chapters_a import CHAPTERS_A
from app.content.solar_system.chapters_b import CHAPTERS_B
from app.content.solar_system.infographics import INFOGRAPHICS
from app.content.solar_system.svg import badge_svg, data_url
from app.db import SessionLocal

CHAPTERS = CHAPTERS_A + CHAPTERS_B
SOURCE_URL = "https://openstax.org/details/books/astronomy-2e"


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

        for chapter in CHAPTERS:
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
            elif not chapter_topic.open_to_all_students:
                # Backfill for chapters created before this flag existed.
                # Not coach-editable, so setting it never clobbers an edit;
                # a coach can still hide a chapter by unpublishing it.
                chapter_topic.open_to_all_students = True
            if not chapter_topic.story_origin and chapter_topic.story_md == chapter["story"]:
                chapter_topic.story_origin = "sourced"

            resource = (
                db.query(models.Resource)
                .filter(models.Resource.topic_id == chapter_topic.id, models.Resource.title == chapter["source_title"])
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

            existing_captions = {
                row[0] for row in db.query(models.Diagram.caption).filter(models.Diagram.topic_id == chapter_topic.id)
            }
            for page, key in enumerate(chapter["infographics"], start=1):
                caption, build = INFOGRAPHICS[key]
                if caption not in existing_captions:
                    db.add(
                        models.Diagram(
                            topic_id=chapter_topic.id,
                            resource_id=resource.id,
                            image_data_url=data_url(build()),
                            caption=caption,
                            page_number=page,
                        )
                    )

            seeded_terms = {concept["term"] for concept in chapter["concepts"]}
            existing = db.query(models.ConceptTerm).filter(models.ConceptTerm.topic_id == chapter_topic.id).all()
            for row in existing:
                # Backfill provenance for cards created before `origin` existed.
                if row.term in seeded_terms and row.origin != "sourced":
                    row.origin = "sourced"
            existing_terms = {row.term for row in existing}
            for concept in chapter["concepts"]:
                if concept["term"] in existing_terms:
                    continue
                label, sub, color = concept["badge"]
                db.add(
                    models.ConceptTerm(
                        topic_id=chapter_topic.id,
                        term=concept["term"],
                        explanation_md=concept["explanation"],
                        analogy=concept["analogy"],
                        why_it_matters=concept["why"],
                        source_resource_ids=[resource.id],
                        approved=True,
                        origin="sourced",
                        image_data_url=data_url(badge_svg(label, sub, color)),
                    )
                )

        db.commit()
    finally:
        db.close()
