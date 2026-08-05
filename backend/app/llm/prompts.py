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
                    "explanation_md": {"type": "string", "description": "2-5 sentences, markdown allowed"},
                    "source": {
                        "type": "string",
                        "enum": ["team_resource", "general_knowledge"],
                        "description": "team_resource if grounded in provided snippets, general_knowledge otherwise",
                    },
                },
                "required": ["term", "explanation_md", "source"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["concepts"],
    "additionalProperties": False,
}


def explanation_prompt(topic_name: str, topic_description: str, labeled_snippets: list[dict]) -> tuple[str, str]:
    system = (
        "You help a Science Olympiad coach prepare students for competition. Given "
        "relevant snippets from the team's own resources (which may be sparse or "
        "absent), produce a glossary of the key concepts and jargon a student must "
        "know for this topic. For each concept: if the provided snippets actually "
        "cover it, ground the explanation in them and mark source as "
        "'team_resource'. If the snippets don't cover it well, still explain it "
        "using your general knowledge of the event, and mark source as "
        "'general_knowledge' -- don't skip important concepts just because the "
        "team's materials didn't happen to cover them, and don't stretch thin "
        "snippets to cover concepts they don't really address."
    )
    snippet_block = "\n\n".join(
        f"[{s['source_type']}] {s['text']}" for s in labeled_snippets
    ) or "(no relevant team resources found)"
    user = (
        f"Topic: {topic_name}\n"
        f"Description: {topic_description}\n\n"
        f"Relevant snippets from team resources:\n{snippet_block}\n\n"
        "Produce 5-10 concept/jargon terms a student competing in this event should know."
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
