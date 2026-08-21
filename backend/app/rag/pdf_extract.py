from pathlib import Path

import pymupdf

from app.llm.router import get_llm_handle

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


def extract_pdf_text(path: Path, coach=None) -> tuple[str, list[dict]]:
    """Extract a PDF's content, handling image-heavy pages, not just text.

    Most pages go through PyMuPDF's plain text extraction (free, instant).
    Pages where that comes back thin -- scans, diagrams, charts -- get
    rendered to an image and described by Gemini instead, so a coach's PDF
    with photos of a whiteboard or a labeled diagram doesn't just get
    silently dropped. Capped at MAX_VISION_PAGES so a large scanned document
    doesn't turn into dozens of LLM calls from one upload.

    Also returns the diagram pages themselves (not just their text
    description) as {"image_bytes", "caption", "page_number"} dicts, so
    callers can surface the actual image as a visual aid instead of
    discarding it once the description is folded into the returned text.
    """
    llm = get_llm_handle(coach)
    doc = pymupdf.open(str(path))
    parts: list[str] = []
    diagrams: list[dict] = []
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
                description = llm.describe_image(_VISION_PROMPT, pixmap.tobytes("png"), label="pdf_page_vision")
                vision_calls += 1
                if description.strip():
                    parts.append(description)
                    # Separate, lower-dpi render just for storage/display --
                    # the dpi=150 PNG above is only ever used for the vision
                    # call itself, so its accuracy is untouched; this is a
                    # much lighter copy sized for showing in a browser gallery.
                    thumb = page.get_pixmap(dpi=96)
                    diagrams.append(
                        {
                            "image_bytes": thumb.tobytes(output="jpg", jpg_quality=85),
                            "caption": description,
                            "page_number": page.number,
                        }
                    )
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
    return result, diagrams
