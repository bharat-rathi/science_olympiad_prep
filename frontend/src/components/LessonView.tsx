import { Fragment, ReactNode, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { ChapterLesson, Diagram, StudyPlan, Topic } from "../api/client";

type WordEntry = { word: string; meaning: string };

// Every way a word-bank entry might be written in the lesson text:
// "Astronomical unit (AU)" -> "astronomical unit", "AU", plus plurals.
function aliasesFor(word: string): string[] {
  const out = new Set<string>();
  const plain = word.replace(/\s*\(.*?\)/g, "").trim();
  const inner = word.match(/\((.*?)\)/)?.[1]?.trim();
  for (const base of [plain, inner]) {
    if (!base || base.length < 2) continue;
    out.add(base);
    if (!/s$/i.test(base) && base.length > 3) out.add(base + "s");
  }
  return [...out];
}

function escapeRegex(s: string) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

// Short all-caps abbreviations (AU, HZ, JWST) must match case exactly so
// "au" inside ordinary words or sentences isn't highlighted.
function isAbbrev(alias: string) {
  return alias.length <= 5 && alias === alias.toUpperCase() && /[A-Z]/.test(alias);
}

export function useJargon(wordBank: WordEntry[]) {
  return useMemo(() => {
    const lookup = new Map<string, WordEntry>();
    const aliases: string[] = [];
    for (const entry of wordBank) {
      for (const alias of aliasesFor(entry.word)) {
        const key = isAbbrev(alias) ? alias : alias.toLowerCase();
        if (!lookup.has(key)) {
          lookup.set(key, entry);
          aliases.push(alias);
        }
      }
    }
    aliases.sort((a, b) => b.length - a.length);
    const regex = aliases.length ? new RegExp(`\\b(${aliases.map(escapeRegex).join("|")})\\b`, "gi") : null;
    return { lookup, regex };
  }, [wordBank]);
}

function JargonWord({ text, entry }: { text: string; entry: WordEntry }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button type="button" className="jargon" title={entry.meaning} aria-expanded={open} onClick={() => setOpen((o) => !o)}>
        {text}
      </button>
      {open && (
        <span className="jargon-def" role="note">
          <strong>{entry.word}:</strong> {entry.meaning}
        </span>
      )}
    </>
  );
}

// Highlight the first appearance of each word-bank word in a block of text.
function highlight(text: string, jargon: ReturnType<typeof useJargon>, seen: Set<WordEntry>): ReactNode[] {
  const { lookup, regex } = jargon;
  if (!regex) return [text];
  const out: ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(regex)) {
    const raw = m[0];
    // Abbreviations are stored in exact case, everything else lowercased, so
    // "au" in ordinary text never matches the "AU" entry.
    const entry = lookup.get(raw) ?? lookup.get(raw.toLowerCase());
    if (!entry || seen.has(entry)) continue;
    seen.add(entry);
    out.push(text.slice(last, m.index));
    out.push(<JargonWord key={`${m.index}-${raw}`} text={raw} entry={entry} />);
    last = (m.index ?? 0) + raw.length;
  }
  out.push(text.slice(last));
  return out;
}

// Plain-text lesson body -> paragraphs, bullet lists and numbered lists.
function RichText({ body, jargon, seen }: { body: string; jargon: ReturnType<typeof useJargon>; seen: Set<WordEntry> }) {
  const blocks: ReactNode[] = [];
  body.split("\n\n").forEach((block, b) => {
    const lines = block.split("\n");
    let i = 0;
    while (i < lines.length) {
      if (lines[i].startsWith("• ")) {
        const items: string[] = [];
        while (i < lines.length && lines[i].startsWith("• ")) items.push(lines[i++].slice(2));
        blocks.push(
          <ul key={`${b}-${i}`} className="lesson-list">
            {items.map((item, k) => (
              <li key={k}>{highlight(item, jargon, seen)}</li>
            ))}
          </ul>,
        );
      } else if (/^\d+\. /.test(lines[i])) {
        const items: string[] = [];
        while (i < lines.length && /^\d+\. /.test(lines[i])) items.push(lines[i++].replace(/^\d+\. /, ""));
        blocks.push(
          <ol key={`${b}-${i}`} className="lesson-list">
            {items.map((item, k) => (
              <li key={k}>{highlight(item, jargon, seen)}</li>
            ))}
          </ol>,
        );
      } else {
        const para: string[] = [];
        while (i < lines.length && !lines[i].startsWith("• ") && !/^\d+\. /.test(lines[i])) para.push(lines[i++]);
        blocks.push(
          <p key={`${b}-${i}`} className="lesson-para">
            {para.map((line, k) => (
              <Fragment key={k}>
                {k > 0 && <br />}
                {highlight(line, jargon, seen)}
              </Fragment>
            ))}
          </p>,
        );
      }
    }
  });
  return <>{blocks}</>;
}

export function LessonReader({
  lesson,
  diagrams,
  onZoom,
}: {
  lesson: ChapterLesson;
  diagrams: Diagram[];
  onZoom: (d: Diagram) => void;
}) {
  const jargon = useJargon(lesson.word_bank);
  const byCaption = new Map(diagrams.map((d) => [d.caption, d]));
  return (
    <div className="lesson">
      <div className="card lesson-goals">
        <strong>By the end of this chapter you can:</strong>
        <ul className="lesson-list">
          {lesson.goals.map((g) => (
            <li key={g}>{g}</li>
          ))}
        </ul>
        <p className="muted" style={{ margin: "8px 0 0" }}>
          Tip: tap any <span className="jargon jargon-sample">underlined word</span> to see what it means.
        </p>
      </div>
      {lesson.sections.map((section, i) => {
        // Highlight each word once per section, so it's explained where it's used.
        const seen = new Set<WordEntry>();
        const diagram = section.infographic ? byCaption.get(section.infographic) : undefined;
        return (
          <section className="card lesson-section" key={section.heading}>
            <span className="lesson-step">Part {i + 1} of {lesson.sections.length}</span>
            <h3>{section.heading}</h3>
            <RichText body={section.body} jargon={jargon} seen={seen} />
            {diagram && (
              <figure className="lesson-figure zoomable" onClick={() => onZoom(diagram)} role="button" tabIndex={0}>
                <img src={diagram.image_data_url} alt={diagram.caption} loading="lazy" />
                <figcaption className="muted">{diagram.caption} (tap to enlarge)</figcaption>
              </figure>
            )}
          </section>
        );
      })}
      <section className="card lesson-section">
        <h3>Note-sheet facts</h3>
        <p className="muted" style={{ marginTop: 0 }}>The numbers and names worth copying onto your note sheet.</p>
        <ul className="lesson-list key-facts">
          {lesson.key_facts.map((fact) => (
            <li key={fact}>{fact}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export function WordBank({ lesson }: { lesson: ChapterLesson }) {
  const [filter, setFilter] = useState("");
  const words = [...lesson.word_bank]
    .sort((a, b) => a.word.localeCompare(b.word))
    .filter((w) => !filter || `${w.word} ${w.meaning}`.toLowerCase().includes(filter.toLowerCase()));
  return (
    <div className="card">
      <input value={filter} onChange={(e) => setFilter(e.target.value)} placeholder="Find a word..." style={{ marginBottom: 12 }} />
      <dl className="word-bank">
        {words.map((w) => (
          <div key={w.word} className="word-bank-row">
            <dt>{w.word}</dt>
            <dd>{w.meaning}</dd>
          </div>
        ))}
      </dl>
      {words.length === 0 && <p className="muted">No words match.</p>}
    </div>
  );
}

export function QuickCheck({ lesson }: { lesson: ChapterLesson }) {
  const [shown, setShown] = useState<Set<number>>(new Set());
  const toggle = (i: number) =>
    setShown((prev) => {
      const next = new Set(prev);
      if (next.has(i)) next.delete(i);
      else next.add(i);
      return next;
    });
  return (
    <div className="stack">
      <p className="muted" style={{ margin: 0 }}>Try to answer in your head (or out loud) first, then check.</p>
      {lesson.quick_check.map((item, i) => (
        <div className="card quick-check" key={item.q}>
          <strong>
            {i + 1}. {item.q}
          </strong>
          {shown.has(i) ? (
            <p className="quick-check-answer">{item.a}</p>
          ) : null}
          <button onClick={() => toggle(i)} style={{ alignSelf: "flex-start" }}>
            {shown.has(i) ? "Hide answer" : "Show answer"}
          </button>
        </div>
      ))}
    </div>
  );
}

export function StudyPlanView({ plan, chapters, parentName }: { plan: StudyPlan; chapters: Topic[]; parentName: string }) {
  const byName = new Map(chapters.map((c) => [c.name, c]));
  let n = 0;
  return (
    <div className="study-plan">
      <h2>Your study plan</h2>
      <div className="card">
        <p style={{ marginTop: 0 }}>{plan.intro}</p>
        <strong>How to study</strong>
        <ul className="lesson-list">
          {plan.how_to_study.map((tip) => (
            <li key={tip}>{tip}</li>
          ))}
        </ul>
      </div>
      {plan.units.map((unit) => (
        <div key={unit.number} className="plan-unit">
          <h3>
            Unit {unit.number}: {unit.title}
          </h3>
          <p className="muted" style={{ marginTop: 0 }}>{unit.summary}</p>
          <div className="grid-2">
            {unit.chapters.map((ch) => {
              n += 1;
              const topic = byName.get(ch.name);
              const label = ch.name.startsWith(`${parentName}: `) ? ch.name.slice(parentName.length + 2) : ch.name;
              const body = (
                <div className={`card ${topic ? "hoverable" : ""}`}>
                  <span className="muted">Chapter {n}</span>
                  <span className="card-title" style={{ display: "block" }}>{label}</span>
                  <p className="muted" style={{ margin: "4px 0 0" }}>{ch.description}</p>
                  {!topic && <p className="muted" style={{ margin: "4px 0 0" }}>(hidden by your coach)</p>}
                </div>
              );
              return topic ? (
                <Link to={`/student/${topic.id}`} key={ch.name} style={{ textDecoration: "none", color: "inherit" }}>
                  {body}
                </Link>
              ) : (
                <div key={ch.name}>{body}</div>
              );
            })}
          </div>
        </div>
      ))}
    </div>
  );
}
