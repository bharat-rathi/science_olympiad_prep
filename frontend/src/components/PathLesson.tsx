import { useState } from "react";
import { Link } from "react-router-dom";
import { Topic } from "../api/client";
import { PathLessonContent, PathPosition } from "../lib/pathLesson";

// One topic of an event's learning path, laid out like the event pages it is
// modeled on: terms you will need, how the topic runs, then each numbered
// section, a check question, and links to the neighbouring topics.
export default function PathLesson({
  content,
  position,
  siblings,
}: {
  content: PathLessonContent;
  position: PathPosition;
  siblings: Topic[];
}) {
  const [showAnswer, setShowAnswer] = useState(false);
  const steps = [
    ...content.sections.map((s, i) => ({ id: `section-${i + 1}`, label: s.heading })),
    ...(content.check ? [{ id: "check", label: "Check yourself" }] : []),
  ];
  const prev = siblings[position.number - 2];
  const next = siblings[position.number];

  return (
    <div className="path-lesson">
      {(content.terms.length > 0 || content.termsText) && (
        <section className="card stack">
          <h2 style={{ margin: 0 }}>Terms you will need</h2>
          {content.terms.length > 0 ? (
            <dl className="path-terms">
              {content.terms.map((t) => (
                <div key={t.term}>
                  <dt>{t.term.charAt(0) + t.term.slice(1).toLowerCase()}</dt>
                  <dd>{t.definition}</dd>
                </div>
              ))}
            </dl>
          ) : (
            <p style={{ margin: 0 }}>{content.termsText}</p>
          )}
        </section>
      )}

      <section className="card stack">
        <h2 style={{ margin: 0 }}>How this topic runs</h2>
        <ol className="path-steps">
          {steps.map((s) => (
            <li key={s.id}>
              <a href={`#${s.id}`}>{s.label}</a>
            </li>
          ))}
        </ol>
      </section>

      {content.sections.map((s, i) => (
        <section className="path-section" id={`section-${i + 1}`} key={s.heading + i}>
          <h2>
            <span className="path-step-number">{i + 1}</span>
            {s.heading}
          </h2>
          {s.body.split(/\n\s*\n/).map((p, j) => (
            <p key={j}>{p}</p>
          ))}
        </section>
      ))}

      {content.check && (
        <section className="path-section" id="check">
          <h2>
            <span className="path-step-number">{steps.length}</span>
            Check yourself
          </h2>
          <div className="card stack">
            <p style={{ margin: 0 }}>{content.check.question}</p>
            {content.check.answer &&
              (showAnswer ? (
                <p className="path-answer">{content.check.answer}</p>
              ) : (
                <button style={{ alignSelf: "flex-start" }} onClick={() => setShowAnswer(true)}>
                  Show answer
                </button>
              ))}
          </div>
        </section>
      )}

      <nav className="row path-nav">
        {prev ? (
          <Link to={`/student/${prev.id}`}>&larr; Topic {position.number - 1}</Link>
        ) : (
          <span />
        )}
        <span className="muted">
          Topic {position.number} of {position.total}
        </span>
        {next ? <Link to={`/student/${next.id}`}>Topic {position.number + 1} &rarr;</Link> : <span />}
      </nav>
    </div>
  );
}
