from pathlib import Path

import pymupdf

from app.llm.client import describe_image

# Below this many characters, treat a page as "not really text" -- a scanned
# page, a diagram, a chart -- rather than trusting a sparse/garbled
# extraction.
MIN_TEXT_CHARS_PER_PAGE = 40
# Cap how many pages per document get a vision call, so one huge scanned PDF
# can't quietly rack up dozens of LLM calls.
MAX_VISION_PAGES = 15

_VISION_PROMPT = (
    "This is a page from a Science Olympiad coaching resource. If it's a scanned "
    "page of text, transcribe the text plainly. If it's a diagram, chart, or "
    "illustration, describe what it shows, including any labeled parts or values, "
    "in plain text a student could read. No commentary, just the content."
)


def extract_pdf_text(path: Path) -> str:
    """Extract a PDF's content, handling image-heavy pages, not just text.

    Most pages go through PyMuPDF's plain text extraction (free, instant).
    Pages where that comes back thin -- scans, diagrams, charts -- get
    rendered to an image and described by Gemini instead, so a coach's PDF
    with photos of a whiteboard or a labeled diagram doesn't just get
    silently dropped. Capped at MAX_VISION_PAGES so a large scanned document
    doesn't turn into dozens of LLM calls from one upload.
    """
    doc = pymupdf.open(str(path))
    parts: list[str] = []
    vision_calls = 0
    try:
        for page in doc:
            text = (page.get_text() or "").strip()
            if len(text) >= MIN_TEXT_CHARS_PER_PAGE:
                parts.append(text)
                continue

            has_images = len(page.get_images()) > 0
            if has_images and vision_calls < MAX_VISION_PAGES:
                pixmap = page.get_pixmap(dpi=150)
                description = describe_image(_VISION_PROMPT, pixmap.tobytes("png"), label="pdf_page_vision")
                vision_calls += 1
                if description.strip():
                    parts.append(description)
            elif text:
                parts.append(text)
    finally:
        doc.close()

    result = "\n\n".join(p for p in parts if p.strip())
    if not result.strip():
        raise ValueError(
            "Couldn't extract any content from that PDF -- it may be empty or unreadable. "
            "Try pasting the text directly instead."
        )
    return result
