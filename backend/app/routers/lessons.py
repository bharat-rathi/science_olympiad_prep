"""Structured lessons and the student "Ask a question" box.

GET  /api/topics/{id}/lesson -- the topic's deterministic lesson (a chapter)
     or study plan (an event), as stored in Topic.lesson_json.
POST /api/topics/{id}/ask    -- answer a student's question from the
     deterministic lessons FIRST: a keyword search over every lesson
     section, word-bank entry, flashcard, quick-check question and note-sheet
     fact the student can see (this chapter ranked first, then its sibling
     chapters), plus the event's rules. No LLM, no embeddings, no API key.
     Only when the student asks for it (use_ai) does an AI tutor answer, and
     even then it is grounded on the best-matching lesson passages and told
     to say when it goes beyond them.
"""

import math
import re

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.db import get_db

router = APIRouter(prefix="/api/topics", tags=["lessons"])

STOPWORDS = set(
    """a an and are as at be been but by can could did do does doing for from had has have how i if in into is it its
    me my of on or so than that the their them then there these they this to was we were what when where which who
    whom why will with would you your about also any just more most much some such very not no yes our out up down
    off over under again why tell explain mean means meaning please know get got make made thing things like many""".split()
)
MAX_MATCHES = 3
SNIPPET_CHARS = 700


def _stem(word: str) -> str:
    for suffix in ("ies", "es", "s", "ing", "ed"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)] + ("y" if suffix == "ies" else "")
    return word


def _tokens(text: str) -> list[str]:
    return [_stem(w) for w in re.findall(r"[a-z0-9]+(?:\.[0-9]+)?", text.lower()) if w not in STOPWORDS and len(w) > 1]


def _plain(word: str) -> str:
    return re.sub(r"\s*\(.*?\)", "", word).strip().lower()


def _passages(topic: models.Topic) -> list[dict]:
    """Every searchable piece of one chapter's lesson."""
    lesson = topic.lesson_json or {}
    if lesson.get("kind") != "lesson":
        return []
    chapter = topic.name.removeprefix("Solar System: ")
    out: list[dict] = []

    def add(kind: str, title: str, text: str, alias: str = "") -> None:
        out.append({"topic_id": topic.id, "chapter": chapter, "kind": kind, "title": title, "text": text, "alias": alias})

    for section in lesson.get("sections", []):
        for paragraph in section["body"].split("\n\n"):
            if paragraph.strip():
                add("lesson", section["heading"], paragraph.strip())
    for entry in lesson.get("word_bank", []):
        add("word", entry["word"], f"{entry['word']}: {entry['meaning']}", alias=_plain(entry["word"]))
    for item in lesson.get("quick_check", []):
        add("quick_check", item["q"], f"Q: {item['q']}\nA: {item['a']}")
    for fact in lesson.get("key_facts", []):
        add("fact", "Note-sheet fact", fact)
    for concept in topic.concepts:
        if concept.approved:
            body = " ".join(part for part in (concept.analogy, concept.explanation_md, concept.why_it_matters) if part)
            add("card", concept.term, f"{concept.term}: {body}", alias=concept.term.lower())
    return out


def _rules_passages(event: models.Topic) -> list[dict]:
    fields = [
        ("What the event is", event.overview_what),
        ("What you need to learn", event.overview_learn),
        ("How it's assessed", event.overview_assessed),
        ("2027 theme", event.overview_theme_2027),
        ("Notes", event.overview_notes),
    ]
    return [
        {"topic_id": event.id, "chapter": f"{event.name} rules", "kind": "rules", "title": title, "text": text, "alias": ""}
        for title, text in fields
        if text
    ]


def _corpus(db: Session, request: Request, topic: models.Topic) -> list[tuple[dict, float]]:
    """(passage, weight) pairs the asker may see: this chapter first, then
    the other chapters of the same event, then the event's rules."""
    student = request.state.student
    event = db.get(models.Topic, topic.parent_topic_id) if topic.parent_topic_id else topic
    chapters = db.query(models.Topic).filter(models.Topic.parent_topic_id == event.id).order_by(models.Topic.id).all()
    if student is not None:
        chapters = [c for c in chapters if auth.student_can_see(db, student, c)]
    corpus: list[tuple[dict, float]] = []
    for chapter in chapters:
        weight = 1.35 if chapter.id == topic.id else 1.0
        corpus += [(p, weight) for p in _passages(chapter)]
    corpus += [(p, 1.4) for p in _rules_passages(event)]
    return corpus


def search_lessons(question: str, corpus: list[tuple[dict, float]], limit: int = MAX_MATCHES) -> list[dict]:
    query = list(dict.fromkeys(_tokens(question)))
    if not query or not corpus:
        return []
    docs = [(p, w, _tokens(p["title"] + " " + p["text"]), set(_tokens(p["title"]))) for p, w in corpus]
    n = len(docs)
    df = {q: sum(1 for _, _, toks, _ in docs if q in toks) for q in query}
    lowered = question.lower()
    scored = []
    for passage, weight, toks, title_toks in docs:
        counts: dict[str, int] = {}
        for t in toks:
            counts[t] = counts.get(t, 0) + 1
        matched = [q for q in query if counts.get(q)]
        if not matched:
            continue
        score = 0.0
        for q in matched:
            idf = math.log(1 + n / (1 + df[q]))
            score += (1 + math.log(counts[q])) * idf * (1.8 if q in title_toks else 1.0)
        coverage = len(matched) / len(query)
        alias = passage["alias"]
        exact = bool(alias) and len(alias) > 2 and re.search(r"\b" + re.escape(alias) + r"\b", lowered) is not None
        if coverage < 0.3 and not exact:
            continue
        score *= coverage
        if exact:
            score += 6.0 + len(alias.split())
        if passage["kind"] == "word" and exact:
            score += 2.0  # "what is X?" -> the word-bank definition first
        score = score * weight / (1 + 0.04 * math.sqrt(len(toks)))
        scored.append((score, passage))
    scored.sort(key=lambda item: -item[0])
    # At most two passages per lesson section, so one long section can't
    # crowd out a word-bank definition or a quick-check answer.
    results, per_section = [], {}
    for _, passage in scored:
        key = (passage["topic_id"], passage["kind"], passage["title"])
        if per_section.get(key, 0) >= 2:
            continue
        per_section[key] = per_section.get(key, 0) + 1
        results.append(passage)
        if len(results) >= limit:
            break
    return results


def ai_tutor_prompt(topic_name: str, passages: list[dict]) -> str:
    notes = "\n\n".join(f"[{p['chapter']} -- {p['title']}]\n{p['text']}" for p in passages) or "(no matching lesson notes)"
    return (
        "You are a friendly science tutor for Science Olympiad students who are 11-12 years old and may not have "
        f"much science background. They are studying '{topic_name}' and asked a question their lesson notes "
        "didn't fully answer.\n\n"
        "Rules:\n"
        "- Use the lesson notes below first, and keep every number and fact consistent with them.\n"
        "- If the notes don't cover the question, you may use well-established astronomy knowledge, but say "
        "clearly: 'This part isn't in your lessons, so check it with your coach.'\n"
        "- Never invent numbers, dates or names. If you're not sure, say so.\n"
        "- Explain every science word in simple, kid-friendly words, and use an everyday comparison when it helps.\n"
        "- Keep it short: about 3-8 sentences, plain text, no markdown headings.\n\n"
        f"Lesson notes:\n{notes}"
    )


@router.get("/{topic_id}/lesson")
def get_lesson(topic_id: int, request: Request, db: Session = Depends(get_db)):
    topic = auth.require_topic_visible(db, request, topic_id)
    if not topic.lesson_json:
        raise HTTPException(404, "This topic has no lesson.")
    return topic.lesson_json


@router.post("/{topic_id}/ask", response_model=schemas.AskResponse)
def ask(topic_id: int, payload: schemas.AskRequest, request: Request, db: Session = Depends(get_db)):
    topic = auth.require_topic_visible(db, request, topic_id)
    if request.state.coach is None and request.state.student is None:
        raise HTTPException(401, "Log in to ask questions.")
    question = payload.question.strip()
    if not question:
        raise HTTPException(400, "Type a question first.")
    question = question[:500]

    corpus = _corpus(db, request, topic)
    matches = search_lessons(question, corpus)
    response = schemas.AskResponse(
        question=question,
        matches=[schemas.AskMatch(**{k: m[k] for k in ("topic_id", "chapter", "kind", "title")}, text=m["text"][:SNIPPET_CHARS]) for m in matches],
    )
    if payload.use_ai:
        grounding = search_lessons(question, corpus, limit=8)
        try:
            from app.llm.router import get_llm_handle

            response.ai_answer = get_llm_handle(request.state.coach).chat_turn(
                ai_tutor_prompt(topic.name, grounding),
                [{"role": "user", "content": question}],
                max_tokens=700,
                effort="low",
                label="lesson_ask_ai",
            )
        except Exception:
            response.ai_error = "The AI tutor isn't available right now. Try again later, or ask your coach."
    return response
