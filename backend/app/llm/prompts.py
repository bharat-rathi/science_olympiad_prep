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
                        "description": "First-principles explanation for a student meeting this concept for the "
                        "first time, 3-6 sentences, markdown allowed",
                    },
                    "analogy": {
                        "type": "string",
                        "description": "One short, concrete real-world comparison that makes the concept click "
                        "-- not a restatement of the explanation, an actual analogy",
                    },
                    "source": {
                        "type": "string",
                        "enum": ["team_resource", "general_knowledge"],
                        "description": "team_resource if grounded in provided snippets, general_knowledge otherwise",
                    },
                },
                "required": ["term", "explanation_md", "analogy", "source"],
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
        "first time -- not to a coach, not to someone with prior background. Write from "
        "first principles: build the idea up from what the student already knows about "
        "the everyday world, define every piece of jargon inline the moment you use it "
        "(never assume a term is already understood), and avoid unexplained notation, "
        "formulas, or domain shorthand. Prefer plain, concrete language over technical "
        "precision -- it's fine to simplify as long as it's not wrong. Given relevant "
        "snippets from the team's own resources (which may be sparse or absent), produce "
        "a glossary of the key concepts and jargon a student must know for this topic. "
        "For each concept: if the provided snippets actually cover it, ground the "
        "explanation in them and mark source as 'team_resource'. If the snippets don't "
        "cover it well, still explain it using your general knowledge of the event, and "
        "mark source as 'general_knowledge' -- don't skip important concepts just "
        "because the team's materials didn't happen to cover them, and don't stretch "
        "thin snippets to cover concepts they don't really address. Also give each "
        "concept a short, concrete analogy to something from ordinary life."
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
        "You research a topic for a Science Olympiad team using web search, then "
        "write up what you found in your own words -- organized, factual notes a "
        "coach can turn into student-facing material, not a copy-paste of any one "
        "page. Search as many times as needed to cover the topic properly. Stick to "
        "material genuinely relevant to the given event/topic; skip tangents. "
        "End your response with a line reading exactly 'Sources:' followed by one "
        "bullet per source actually used, each formatted exactly as "
        "'- <title> -- <url>'."
    )
    user = (
        f"Event/topic: {topic_name}\n"
        f"Topic description: {topic_description}\n\n"
        f"Research this: {query}\n\n"
        "Write organized notes covering the key facts and concepts a student would "
        "need to know, then the Sources section."
    )
    return system, user


def image_prompt(topic_name: str, term: str, analogy: str) -> str:
    """Review agent's visual step: one illustration prompt for a flashcard concept.

    Plain string, not JSON -- generate_image() takes a text prompt directly.
    """
    analogy_hint = f" Lean on this analogy if it suggests a clear scene: {analogy}." if analogy else ""
    return (
        f"A simple, friendly, colorful educational illustration for a Science Olympiad "
        f"flashcard explaining '{term}' (from the topic '{topic_name}') to a middle/high "
        f"school student.{analogy_hint} Flat vector style, clear and uncluttered, no text "
        "or labels or letters anywhere in the image, safe and appropriate for kids."
    )


REFINE_CONCEPT_SCHEMA = {
    "type": "object",
    "properties": {
        "explanation_md": {"type": "string"},
        "analogy": {"type": "string"},
    },
    "required": ["explanation_md", "analogy"],
    "additionalProperties": False,
}


def refine_concept_prompt(
    topic_name: str, term: str, explanation_md: str, analogy: str, feedback: str
) -> tuple[str, str]:
    """Revise one concept's explanation/analogy per a coach's freeform feedback.

    Deliberately does not re-run retrieval -- the concept is already grounded;
    revising wording per feedback doesn't need new source material, so this
    stays a single cheap call instead of a full re-generation.
    """
    system = (
        "You revise a single Science Olympiad concept explanation for a student "
        "audience, based on a coach's feedback. Keep it first-principles and "
        "jargon-free unless the feedback says otherwise. Produce a complete revised "
        "explanation and analogy, not just the delta."
    )
    user = (
        f"Topic: {topic_name}\n"
        f"Concept: {term}\n\n"
        f"Current explanation:\n{explanation_md}\n\n"
        f"Current analogy:\n{analogy or '(none yet)'}\n\n"
        f"Coach feedback:\n{feedback}\n\n"
        "Revise the explanation and analogy to address this feedback."
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
