"""Shared shape for the per-event learning paths.

Each lesson is (title, description, text). The text always runs in the
same four parts -- key terms, a plain-language start, competition-depth
detail tied to the 2027 rules, and a short check -- so every chapter reads
the same way.
"""


def lesson(title: str, description: str, terms: str, start: str, depth: str, check: str) -> tuple[str, str, str]:
    text = f"KEY TERMS: {terms}\n\nSTART HERE: {start}\n\nAT COMPETITION DEPTH: {depth}\n\nCHECK: {check}"
    return (title, description, text)
