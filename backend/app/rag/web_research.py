import re

from google.genai import errors as genai_errors

from app.llm.client import complete_text_grounded
from app.llm.prompts import research_prompt

_SOURCES_HEADER_RE = re.compile(r"\n\s*Sources:\s*\n?", re.IGNORECASE)
_SOURCE_LINE_RE = re.compile(r"^[-*]\s*(.+?)\s*--\s*(https?://\S+)\s*$")


def research_topic(query: str, topic_name: str, topic_description: str) -> dict:
    """Research agent: look up `query` on the web and synthesize findings.

    Uses Gemini's Google Search grounding tool (complete_text_grounded) so
    the model can look things up rather than answering purely from training
    data. Returns {"title", "text", "sources"} -- `text` is body content only
    (the trailing "Sources:" section is parsed out and returned separately),
    ready to be chunked/embedded like any other resource's raw_text.
    """
    if not query.strip():
        raise ValueError("Nothing to research -- type a topic or keyword.")

    system, user = research_prompt(query, topic_name, topic_description)
    try:
        raw = complete_text_grounded(system, user, max_tokens=3000, effort="high", label="research_topic")
    except genai_errors.APIError as e:
        # Surfaced to the coach instead of a raw 500 -- most likely cause is
        # Google Search grounding not being available on the API key's
        # current tier/quota (see llm/client.py's generate_image docstring
        # for the same caveat on image generation).
        raise ValueError(f"Research failed ({e.code}: {e.message}) -- try again, or paste a link instead.") from e

    parts = _SOURCES_HEADER_RE.split(raw, maxsplit=1)
    body = parts[0].strip()
    if not body:
        raise ValueError(f"Couldn't find anything useful on '{query}' -- try a more specific topic or paste a link instead.")

    sources = []
    if len(parts) > 1:
        for line in parts[1].splitlines():
            match = _SOURCE_LINE_RE.match(line.strip())
            if match:
                sources.append({"title": match.group(1), "url": match.group(2)})

    return {"title": query.strip(), "text": body, "sources": sources}
