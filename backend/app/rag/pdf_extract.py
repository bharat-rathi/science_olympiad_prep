from pathlib import Path

from pypdf import PdfReader


def extract_pdf_text(path: Path) -> str:
    """Extract text from a PDF -- no LLM involved, same as the plain-text path."""
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n\n".join(p for p in pages if p.strip())
    if not text.strip():
        raise ValueError(
            "Couldn't extract any text from that PDF -- it may be a scanned image "
            "without a text layer. Try pasting the text directly instead."
        )
    return text
