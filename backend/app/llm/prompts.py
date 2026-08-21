"""Prompt templates for every LLM call in the pipeline.

Kept in one file, separate from the calling code, so the exact wording used
for each step (relevance judging, explanation, quiz generation, hints,
tutoring) is easy to find and tune independently.
"""

RELEVANCE_SCHEMA = {
    "type": "object",
    "properties": {
        "score": {"type": "number", "description": "0.0 (irrelevant) to 1.0 (highly relevant)"},
        "reason": {"type": "string"},
    },
    "required": ["score", "reason"],
    "additionalProperties": False,
}


def relevance_judge_prompt(topic_name: str, topic_description: str, source_type: str, chunk_text: str) -> tuple[str, str]:
    system = (
        "You judge whether a snippet of source material substantively explains a "
        "Science Olympiad competition concept a student needs to understand, as "
        "opposed to being competition logistics, rules, schedules, small talk, or "
        "otherwise off-topic. Video transcripts get no special treatment over text "
        "resources -- judge purely on content."
    )
    user = (
        f"Topic: {topic_name}\n"
        f"Topic description: {topic_description}\n"
        f"Source type: {source_type}\n\n"
        f"Snippet:\n{chunk_text}\n\n"
        "Score how substantively this snippet explains a concept the student needs "
        "for this topic (0.0-1.0), and give a one-sentence reason."
    )
    return system, user


BATCH_RELEVANCE_SCHEMA = {
    "type": "object",
    "properties": {
        "judgments": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "score": {"type": "number", "description": "0.0 (irrelevant) to 1.0 (highly relevant)"},
                    "reason": {"type": "string"},
                },
                "required": ["index", "score", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["judgments"],
    "additionalProperties": False,
}


def batch_relevance_judge_prompt(
    topic_name: str, topic_description: str, candidates: list[dict]
) -> tuple[str, str]:
    """Same rubric as relevance_judge_prompt, but scores every candidate in one call.

    `candidates` items are {"index": int, "source_type": str, "text": str}.
    """
    system = (
        "You judge whether each snippet of source material substantively explains a "
        "Science Olympiad competition concept a student needs to understand, as "
        "opposed to being competition logistics, rules, schedules, small talk, or "
        "otherwise off-topic. Video transcripts get no special treatment over text "
        "resources -- judge purely on content. Score every snippet independently and "
        "return one judgment per snippet, in the same order, each carrying its index."
    )
    snippet_block = "\n\n".join(
        f"[index={c['index']}, source={c['source_type']}]\n{c['text']}" for c in candidates
    )
    user = (
        f"Topic: {topic_name}\n"
        f"Topic description: {topic_description}\n\n"
        f"Snippets:\n{snippet_block}\n\n"
        "For each snippet, score how substantively it explains a concept the student "
        "needs for this topic (0.0-1.0), and give a one-sentence reason."
    )
    return system, user


CONCEPT_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "concepts": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "term": {"type": "string"},
                    "explanation_md": {
                        "type": "string",
                        "description": "The plain-English core idea for a reader with zero prior science "
                        "background meeting this concept for the first time, 2-4 short sentences, one idea at "
                        "a time -- not the analogy and not the event-relevance, those are separate fields below",
                    },
                    "analogy": {
                        "type": "string",
                        "description": "One short, concrete real-world comparison that makes the concept click "
                        "-- not a restatement of the explanation, an actual analogy",
                    },
                    "why_it_matters": {
                        "type": "string",
                        "description": "1-2 sentences tying this concept directly to the actual competition "
                        "event/task (e.g. a specific build decision or scoring rule it affects) -- concrete and "
                        "specific to this event, not a generic 'this is important in physics' statement",
                    },
                    "source": {
                        "type": "string",
                        "enum": ["team_resource", "general_knowledge"],
                        "description": "team_resource if grounded in provided snippets, general_knowledge otherwise",
                    },
                },
                "required": ["term", "explanation_md", "analogy", "why_it_matters", "source"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["concepts"],
    "additionalProperties": False,
}


def explanation_prompt(topic_name: str, topic_description: str, labeled_snippets: list[dict]) -> tuple[str, str]:
    system = (
        "You explain Science Olympiad concepts to a student meeting them for the very "
        "first time -- assume zero prior science background, not just 'new to this "
        "specific topic'. Write from first principles: build the idea up from what the "
        "student already knows about the everyday world, define every piece of jargon "
        "inline the moment you use it (never assume a term is already understood), and "
        "avoid unexplained notation, formulas, or domain shorthand. Prefer plain, "
        "concrete language over technical precision -- it's fine to simplify as long as "
        "it's not wrong. Given relevant snippets from the team's own resources (which "
        "may be sparse or absent), produce a glossary of the key concepts and jargon a "
        "student must know for this topic. For each concept: if the provided snippets "
        "actually cover it, ground the explanation in them and mark source as "
        "'team_resource'. If the snippets don't cover it well, still explain it using "
        "your general knowledge of the event, and mark source as 'general_knowledge' -- "
        "don't skip important concepts just because the team's materials didn't happen "
        "to cover them, and don't stretch thin snippets to cover concepts they don't "
        "really address. Each concept has three distinct parts, each doing one job -- "
        "don't blend them together: explanation_md is the plain idea itself, analogy is "
        "a short relatable comparison, and why_it_matters is a concrete sentence or two "
        "connecting the concept to an actual decision or rule in this specific event "
        "(not a generic statement about physics being useful)."
    )
    snippet_block = "\n\n".join(
        f"[{s['source_type']}] {s['text']}" for s in labeled_snippets
    ) or "(no relevant team resources found)"
    user = (
        f"Topic: {topic_name}\n"
        f"Description: {topic_description}\n\n"
        f"Relevant snippets from team resources:\n{snippet_block}\n\n"
        "Produce 5-10 concept/jargon terms a student new to this event should know, "
        "explained from first principles."
    )
    return system, user


def research_prompt(query: str, topic_name: str, topic_description: str) -> tuple[str, str]:
    """Research agent: search the web for a coach-typed keyword/topic and
    synthesize findings, with a machine-parseable source list at the end.

    Freeform text output (not a JSON schema) -- Google Search grounding and
    schema-constrained JSON output aren't combinable in one call, and the
    trailing "Sources:" section is simple enough for rag/web_research.py to
    parse with a regex.
    """
    system = (
        "You are a research assistant for a Science Olympiad coach, with a Google Search "
        "tool available. Use it -- issue one or more real searches for this topic before "
        "writing anything; do not answer from memory alone and do not just restate or "
        "lightly rephrase the query. Read what the searches actually return, then write a "
        "substantive briefing in your own words: concrete facts, mechanisms, definitions, "
        "and examples a coach could turn into flashcards for a student meeting this topic "
        "for the first time. Aim for several solid paragraphs when the topic has anything "
        "findable. If your searches genuinely turn up nothing useful, say so explicitly in "
        "one sentence rather than padding with generic filler. "
        "End your response with a line reading exactly 'Sources:' followed by one "
        "bullet per source actually used, each formatted exactly as "
        "'- <title> -- <url>'."
    )
    user = (
        f"Event/topic: {topic_name}\n"
        f"Topic description: {topic_description}\n\n"
        f"Search the web and research this: {query}\n\n"
        "Write the briefing covering the key facts and concepts a student would need to "
        "know, then the Sources section."
    )
    return system, user


def image_prompt(topic_name: str, term: str, explanation_md: str, analogy: str) -> str:
    """Review agent's visual step: one illustration prompt for a flashcard concept.

    Grounded in the actual explanation, not just the term -- otherwise the
    image model has almost nothing to depict and falls back to generic
    decoration instead of something that actually explains the concept.
    Plain string, not JSON -- generate_image() takes a text prompt directly.
    """
    analogy_hint = f" It may help to lean on this analogy: {analogy}." if analogy else ""
    return (
        f"Create a labeled explainer diagram (like one from a science textbook, not a "
        f"decorative illustration) for a Science Olympiad student meeting '{term}' for "
        f"the first time, as part of the topic '{topic_name}'. Depict only what's "
        "necessary to make the concept below click at a glance -- the real objects, "
        "motion, or forces involved, shown clearly via genuine diagram conventions: "
        "labeled arrows (e.g. force or motion direction), a labeled before/after pair, "
        "or a labeled cross-section, whichever actually fits this concept. This is a "
        f"focused diagram, not a busy scene with unrelated decorative elements.{analogy_hint}\n\n"
        f"What it needs to explain:\n{explanation_md}\n\n"
        "Style: simple, colorful, flat vector diagram on a plain or minimal background, "
        "clear and uncluttered, friendly and appropriate for kids. A small amount of "
        "in-image text is allowed and encouraged where it aids understanding -- up to "
        "3-4 short labels total (1-3 words each, e.g. a force name, 'before'/'after', a "
        f"key value), placed clearly next to what they label. If a label uses this "
        f"concept's own name, spell it exactly as given here, character for character: "
        f"'{term}' -- do not rely on memory for technical spelling. Labels only, not "
        "full sentences: do not add a caption, title, speech bubble, or any text longer "
        "than a few words anywhere in the image."
    )


REFINE_CONCEPT_SCHEMA = {
    "type": "object",
    "properties": {
        "explanation_md": {"type": "string"},
        "analogy": {"type": "string"},
        "why_it_matters": {"type": "string"},
    },
    "required": ["explanation_md", "analogy", "why_it_matters"],
    "additionalProperties": False,
}


def refine_concept_prompt(
    topic_name: str, term: str, explanation_md: str, analogy: str, why_it_matters: str, feedback: str
) -> tuple[str, str]:
    """Revise one concept's explanation/analogy/why-it-matters per a coach's
    freeform feedback.

    Deliberately does not re-run retrieval -- the concept is already grounded;
    revising wording per feedback doesn't need new source material, so this
    stays a single cheap call instead of a full re-generation.
    """
    system = (
        "You revise a single Science Olympiad concept explanation for a student "
        "audience with zero prior science background, based on a coach's feedback. "
        "Keep it first-principles and jargon-free unless the feedback says otherwise. "
        "The concept has three distinct parts -- explanation_md (the plain idea), "
        "analogy (a relatable comparison), and why_it_matters (how it connects to an "
        "actual decision/rule in this event) -- keep them distinct rather than blending "
        "them. Produce complete revised versions of all three, not just the delta, even "
        "if the feedback only concerns one of them."
    )
    user = (
        f"Topic: {topic_name}\n"
        f"Concept: {term}\n\n"
        f"Current explanation:\n{explanation_md}\n\n"
        f"Current analogy:\n{analogy or '(none yet)'}\n\n"
        f"Current why-it-matters:\n{why_it_matters or '(none yet)'}\n\n"
        f"Coach feedback:\n{feedback}\n\n"
        "Revise the explanation, analogy, and why-it-matters to address this feedback."
    )
    return system, user


STORY_SCHEMA = {
    "type": "object",
    "properties": {"story_md": {"type": "string"}},
    "required": ["story_md"],
    "additionalProperties": False,
}


def story_prompt(topic_name: str, concepts: list[dict]) -> tuple[str, str]:
    system = (
        "You write a short narrative story for Science Olympiad students that weaves "
        "together a set of approved concepts for one topic, in the order given, so a "
        "student can follow the ideas as a story rather than a list of definitions. "
        "Keep it first-principles and concrete -- a student meeting these ideas for "
        "the first time should come away understanding them, not just entertained. "
        "300-600 words, markdown allowed, no section headers -- just flowing narrative."
    )
    concept_block = "\n\n".join(f"### {c['term']}\n{c['explanation_md']}" for c in concepts)
    user = (
        f"Topic: {topic_name}\n\n"
        f"Approved concepts to weave into the story, in this order:\n{concept_block}\n\n"
        "Write the story."
    )
    return system, user


QUIZ_SCHEMA = {
    "type": "object",
    "properties": {
        "questions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "prompt": {"type": "string"},
                    "type": {"type": "string", "enum": ["mcq", "short"]},
                    "choices": {"type": "array", "items": {"type": "string"}},
                    "correct_answer": {"type": "string"},
                    "explanation": {"type": "string"},
                },
                "required": ["prompt", "type", "choices", "correct_answer", "explanation"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["questions"],
    "additionalProperties": False,
}


def quiz_prompt(topic_name: str, concepts: list[dict], num_mcq: int, num_short: int) -> tuple[str, str]:
    system = (
        "You write competition-practice assessment questions for a Science "
        "Olympiad team, grounded strictly in the approved concept explanations "
        "given to you. For mcq questions, 'choices' has 4 options and "
        "'correct_answer' is one of them verbatim. For short questions, "
        "'choices' is an empty array."
    )
    concept_block = "\n\n".join(f"### {c['term']}\n{c['explanation_md']}" for c in concepts)
    user = (
        f"Topic: {topic_name}\n\n"
        f"Approved concept explanations:\n{concept_block}\n\n"
        f"Write exactly {num_mcq} multiple-choice questions and {num_short} short-answer "
        "questions testing these concepts."
    )
    return system, user


def hint_prompt(topic_name: str, concept_context: str, question_prompt: str) -> tuple[str, str]:
    system = (
        "You give a Science Olympiad student a single short hint for a practice "
        "question. The hint must nudge them toward the relevant concept without "
        "revealing the answer. One or two sentences."
    )
    user = (
        f"Topic: {topic_name}\n"
        f"Relevant concept material:\n{concept_context}\n\n"
        f"Question: {question_prompt}\n\n"
        "Give one hint."
    )
    return system, user


def topic_qa_system_prompt(topic_name: str, labeled_snippets: list[dict]) -> str:
    """System prompt for the free-form "ask about this topic's content" chat.

    Grounded strictly in retrieved snippets rather than general knowledge
    (unlike explanation_prompt, which falls back to general knowledge when
    team resources don't cover a concept) -- the point of this feature is to
    answer from what the team actually uploaded, and say so plainly when it
    doesn't cover the question.
    """
    snippet_block = "\n\n".join(f"[{s['source_type']}] {s['text']}" for s in labeled_snippets) or "(no relevant team resources found)"
    return (
        "You are a helpful assistant answering a Science Olympiad student's or coach's "
        f"questions about the topic '{topic_name}', grounded strictly in the team's own "
        "uploaded materials below. Answer using only this material. If the material doesn't "
        "cover the question, say so clearly and explain what's missing -- do not fill the gap "
        "with general knowledge. Keep answers concise (2-5 sentences) unless the question "
        "needs more.\n\n"
        f"Team's uploaded material relevant to this question:\n{snippet_block}"
    )


def tutor_system_prompt(topic_name: str, concept_context: str, question_prompt: str, correct_answer: str, student_answer: str) -> str:
    return (
        "You are a patient, Socratic Science Olympiad tutor. The student just "
        f"answered a practice question incorrectly on the topic '{topic_name}'. "
        "Your job is to help them understand the underlying concept through "
        "conversation -- ask guiding questions, don't just lecture, and don't "
        "simply restate the correct answer unless they're clearly stuck after "
        "genuine effort. Keep each reply short (2-4 sentences).\n\n"
        f"Relevant concept material:\n{concept_context}\n\n"
        f"Question: {question_prompt}\n"
        f"Correct answer: {correct_answer}\n"
        f"Student's (incorrect) answer: {student_answer}"
    )
