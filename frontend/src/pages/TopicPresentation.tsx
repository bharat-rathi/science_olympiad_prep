import { useEffect, useMemo, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, ConceptTerm, Topic } from "../api/client";
import TitleChapter from "../components/presentation/TitleChapter";
import ConceptChapter from "../components/presentation/ConceptChapter";
import SummaryChapter from "../components/presentation/SummaryChapter";
import { getConceptBeats } from "../components/presentation/conceptBeats";
import "../components/presentation/PresentationStage.css";

type Chapter = { kind: "title" } | { kind: "concept"; concept: ConceptTerm; index: number } | { kind: "summary" };

// Global step counter driving pure-function chapters -- ported from
// CHAPTER-CRAFT.md's core architecture (.claude/skills/web-video-presentation):
// each chapter's step count is derived from its own content (a concept with
// no analogy or why_it_matters simply takes fewer steps), and the whole
// presentation is just "which step are we on," never imperative state.
export default function TopicPresentation() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [step, setStep] = useState(0);

  useEffect(() => {
    api.getTopic(id).then(setTopic);
    api.listConcepts(id).then((all) => setConcepts(all.filter((c) => c.approved)));
  }, [id]);

  const chapters: Chapter[] = useMemo(
    () => [{ kind: "title" }, ...concepts.map((concept, index) => ({ kind: "concept" as const, concept, index })), { kind: "summary" }],
    [concepts],
  );

  const chapterStepCounts = useMemo(
    () => chapters.map((c) => (c.kind === "concept" ? getConceptBeats(c.concept).length : 1)),
    [chapters],
  );
  const totalSteps = chapterStepCounts.reduce((a, b) => a + b, 0);

  const chapterStartSteps = useMemo(() => {
    const starts: number[] = [];
    let acc = 0;
    for (const count of chapterStepCounts) {
      starts.push(acc);
      acc += count;
    }
    return starts;
  }, [chapterStepCounts]);

  function locate(globalStep: number): { chapterIndex: number; localStep: number } {
    for (let i = chapters.length - 1; i >= 0; i--) {
      if (globalStep >= chapterStartSteps[i]) return { chapterIndex: i, localStep: globalStep - chapterStartSteps[i] };
    }
    return { chapterIndex: 0, localStep: 0 };
  }

  function goTo(next: number) {
    setStep(Math.max(0, Math.min(totalSteps - 1, next)));
  }

  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "ArrowRight" || e.key === " ") goTo(step + 1);
      else if (e.key === "ArrowLeft") goTo(step - 1);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  });

  if (!topic) return <p>Loading...</p>;

  if (concepts.length === 0) {
    return (
      <div className="pres-page">
        <p className="muted" style={{ color: "#fff" }}>
          No approved concepts yet -- nothing to present for this topic.
        </p>
        <Link to={`/student/${id}`}>
          <button className="primary" style={{ marginTop: 16 }}>
            Back
          </button>
        </Link>
      </div>
    );
  }

  const { chapterIndex, localStep } = locate(step);
  const current = chapters[chapterIndex];

  return (
    <div className="pres-page">
      <Link to={`/student/${id}`} className="pres-exit">
        <button>Exit</button>
      </Link>

      <div className="pres-stage" onClick={() => goTo(step + 1)} role="button" tabIndex={0}>
        {current.kind === "title" && <TitleChapter eventName={topic.event_name} name={topic.name} description={topic.description} />}
        {current.kind === "concept" && <ConceptChapter concept={current.concept} localStep={localStep} index={current.index} total={concepts.length} />}
        {current.kind === "summary" && <SummaryChapter topicName={topic.name} concepts={concepts} />}
      </div>

      <div className="pres-controls">
        <div className="pres-dial">
          {chapters.map((c, i) => (
            <button
              key={i}
              className={`pres-dot ${i === chapterIndex ? "active" : ""}`}
              onClick={(e) => {
                e.stopPropagation();
                goTo(chapterStartSteps[i]);
              }}
              aria-label={c.kind === "concept" ? c.concept.term : c.kind}
            />
          ))}
        </div>
      </div>
      <p className="pres-hint">Click, → / ←, or space to navigate</p>
    </div>
  );
}
