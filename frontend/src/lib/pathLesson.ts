// Learning-path chapters (backend content/learning_paths and Hovercraft's
// path) are named "<Event> N of M: Title" and hold one study-notes resource
// written in labeled paragraphs ("KEY TERMS: ...", "START HERE: ...",
// "AT COMPETITION DEPTH: ...", "CHECK: ..."). These helpers turn that into
// the sectioned topic page the event pages are modeled on.

export interface PathPosition {
  event: string;
  number: number;
  total: number;
  title: string;
}

const PATH_NAME = /^(.+) (\d+) of (\d+): (.+)$/;

export function parsePathName(name: string): PathPosition | null {
  const m = PATH_NAME.exec(name);
  if (!m) return null;
  return { event: m[1], number: Number(m[2]), total: Number(m[3]), title: m[4] };
}

export interface Term {
  term: string;
  definition: string;
}

export interface PathSection {
  heading: string;
  body: string;
}

export interface PathLessonContent {
  terms: Term[];
  // Shown as-is when the key-terms paragraph doesn't split into terms.
  termsText: string;
  sections: PathSection[];
  check: { question: string; answer: string } | null;
}

const LABELED = /^([A-Z][A-Z0-9 '&/-]+):\s*([\s\S]*)$/;

const HEADINGS: Record<string, string> = {
  "START HERE": "Start here",
  "AT COMPETITION DEPTH": "At competition depth",
};

function titleCase(label: string): string {
  return label.charAt(0) + label.slice(1).toLowerCase();
}

// "FORCE -- a push or pull ... AREA -- the size ..." -> one entry per term.
// A term is an upper-case name (optionally with a short parenthetical) right
// before " -- ".
function splitTerms(text: string): Term[] {
  const re = /(?:^|\s)([A-Z][A-Z0-9'/&+ -]*[A-Z0-9](?:\s*\([^()]{1,40}\))?)\s+--\s+/g;
  const hits: { term: string; start: number; end: number }[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(text))) {
    const start = m.index + (m[0].length - m[0].trimStart().length);
    hits.push({ term: m[1], start, end: re.lastIndex });
  }
  return hits.map((h, i) => ({
    term: h.term,
    definition: text.slice(h.end, i + 1 < hits.length ? hits[i + 1].start : text.length).trim(),
  }));
}

// "Question text? (Answer.)" -> the trailing parenthetical is the answer.
function splitCheck(text: string): { question: string; answer: string } {
  const m = /^([\s\S]*?)\s*\(((?:[^()]|\([^()]*\))*)\)\s*$/.exec(text);
  if (!m || !m[1].trim()) return { question: text, answer: "" };
  return { question: m[1].trim(), answer: m[2].trim() };
}

export function parsePathLesson(raw: string): PathLessonContent | null {
  const content: PathLessonContent = { terms: [], termsText: "", sections: [], check: null };
  let sawLabel = false;
  for (const paragraph of raw.split(/\n\s*\n/)) {
    const text = paragraph.trim();
    if (!text) continue;
    const m = LABELED.exec(text);
    if (!m) {
      // Unlabeled paragraph: continue the previous section.
      const last = content.sections[content.sections.length - 1];
      if (last) last.body += `\n\n${text}`;
      else content.sections.push({ heading: "Overview", body: text });
      continue;
    }
    sawLabel = true;
    const [, label, body] = m;
    if (label === "KEY TERMS") {
      content.termsText = body.trim();
      content.terms = splitTerms(content.termsText);
    } else if (label === "CHECK") {
      content.check = splitCheck(body.trim());
    } else {
      content.sections.push({ heading: HEADINGS[label] ?? titleCase(label), body: body.trim() });
    }
  }
  return sawLabel ? content : null;
}
