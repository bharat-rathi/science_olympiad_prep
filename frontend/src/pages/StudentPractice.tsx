import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, ASSESSMENT_TYPE_LABELS, ASSESSMENT_TYPE_TAG_CLASS, Assessment, ConceptTerm, Diagram, Lesson, Resource, Topic } from "../api/client";
import AskQuestions from "../components/AskQuestions";
import { LessonReader, QuickCheck, StudyPlanView, WordBank } from "../components/LessonView";
import TopicChat from "../components/TopicChat";
import TopicOverview from "../components/TopicOverview";

function sourceTag(c: ConceptTerm): string {
  if (c.origin === "sourced") return "from the source reader";
  if (c.origin === "coach") return "edited by your coach";
  if (c.video_relevant) return "from team video";
  return c.source_resource_ids.length ? "from team resource" : "general knowledge";
}

export default function StudentPractice() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [diagrams, setDiagrams] = useState<Diagram[]>([]);
  // Deterministic source material (seeded wiki excerpts / source-reader fact
  // sheets) -- published to students as-is, no coach step.
  const [sourceNotes, setSourceNotes] = useState<Resource[]>([]);
  type View = "lesson" | "words" | "flashcards" | "quiz" | "story" | "notes";
  const [view, setView] = useState<View>("lesson");
  // Structured deterministic lesson (a chapter) or study plan (an event).
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [accessError, setAccessError] = useState("");
  // Diagram tiles are small; infographics need a full-size view to be readable.
  const [zoomed, setZoomed] = useState<Diagram | null>(null);
  // Chapters (sub-topics) this student can open, listed inside the event --
  // e.g. the Solar System learning chapters live here, not on Home.
  const [chapters, setChapters] = useState<Topic[]>([]);
  const [parent, setParent] = useState<Topic | null>(null);

  useEffect(() => {
    setAccessError("");
    setView("lesson");
    setLesson(null);
    api
      .getTopic(id)
      .then(setTopic)
      .catch((err) => setAccessError(err instanceof Error ? err.message : String(err)));
    api.listConcepts(id).then((all) => setConcepts(all.filter((c) => c.approved)));
    // Assessment visibility is independent of the topic's learning-content
    // publish flag -- a coach can publish a test without (or before)
    // publishing the concepts/story, and vice versa.
    api.getLatestAssessment(id).then((a) => setAssessment(a && a.status === "published" ? a : null));
    api.listDiagrams(id).then(setDiagrams);
    api.listSubTopics(id).then(setChapters).catch(() => setChapters([]));
    api
      .listResources(id)
      .then((all) => setSourceNotes(all.filter((r) => r.deterministic && r.raw_text.trim())))
      .catch(() => setSourceNotes([]));
  }, [id]);

  useEffect(() => {
    if (topic?.has_lesson && topic.id === id) {
      api.getLesson(id).then(setLesson).catch(() => setLesson(null));
    }
  }, [topic, id]);

  useEffect(() => {
    setParent(null);
    if (topic?.parent_topic_id) {
      api.getTopic(topic.parent_topic_id).then(setParent).catch(() => setParent(null));
    }
  }, [topic?.parent_topic_id]);

  useEffect(() => {
    if (!zoomed) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") setZoomed(null);
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [zoomed]);

  if (accessError) {
    return (
      <div className="auth-shell">
        <div className="auth-logo">🔒</div>
        <h1>No access to this topic</h1>
        <p className="muted">Ask your coach to assign this topic to you.</p>
      </div>
    );
  }

  if (!topic) return <p>Loading...</p>;

  const chapterLesson = lesson?.kind === "lesson" ? lesson : null;
  const plan = lesson?.kind === "plan" ? lesson : null;
  const learningLive = topic.content_published && (concepts.length > 0 || !!topic.story_md);
  // A structured lesson replaces the older Story / Source notes views (they
  // hold the same text), so students see each piece of content once.
  const views: { key: View; label: string; show: boolean }[] = [
    { key: "lesson", label: "Lesson", show: !!chapterLesson },
    { key: "words", label: `Word bank (${chapterLesson?.word_bank.length ?? 0})`, show: !!chapterLesson },
    { key: "flashcards", label: `Flashcards (${concepts.length})`, show: learningLive && concepts.length > 0 },
    { key: "quiz", label: "Quick check", show: !!chapterLesson && chapterLesson.quick_check.length > 0 },
    { key: "story", label: "Story", show: !chapterLesson && learningLive && !!topic.story_md },
    { key: "notes", label: "Source notes", show: !chapterLesson && sourceNotes.length > 0 },
  ];
  const available = views.filter((v) => v.show);
  const activeView = available.some((v) => v.key === view) ? view : available[0]?.key;
  const nothingYet = available.length === 0 && chapters.length === 0;
  const hasLessons = !!topic.has_lesson || !!parent?.has_lesson;

  return (
    <div>
      <div className="page-header">
        {parent && (
          <Link to={`/student/${parent.id}`} className="muted">
            &larr; Back to {parent.name}
          </Link>
        )}
        {chapterLesson && (
          <span className="lesson-unit">
            Unit {chapterLesson.unit}: {chapterLesson.unit_title}
          </span>
        )}
        <h1>{topic.name}</h1>
        <p className="muted">{topic.description}</p>
        <span className={`tag ${ASSESSMENT_TYPE_TAG_CLASS[topic.assessment_type]}`}>
          {ASSESSMENT_TYPE_LABELS[topic.assessment_type]}
        </span>
      </div>

      <TopicOverview topic={topic} />

      {assessment && (
        <div className="card row" style={{ justifyContent: "space-between" }}>
          <span>A practice test is ready for this topic.</span>
          <Link to={`/student/${id}/test/${assessment.id}`}>
            <button className="primary">Start test</button>
          </Link>
        </div>
      )}

      {plan && <StudyPlanView plan={plan} chapters={chapters} parentName={topic.name} />}

      {!plan && chapters.length > 0 && (
        <>
          <h2>Chapters</h2>
          <div className="grid-2" style={{ marginBottom: 24 }}>
            {chapters.map((c, i) => (
              <Link to={`/student/${c.id}`} key={c.id} style={{ textDecoration: "none", color: "inherit" }}>
                <div className="card hoverable">
                  <span className="muted">Chapter {i + 1}</span>
                  <span className="card-title" style={{ display: "block" }}>
                    {c.name.startsWith(`${topic.name}: `) ? c.name.slice(topic.name.length + 2) : c.name}
                  </span>
                  {c.description && <p className="muted" style={{ margin: "4px 0 0" }}>{c.description}</p>}
                </div>
              </Link>
            ))}
          </div>
        </>
      )}

      {nothingYet && (
        <div className="card">
          <p className="muted" style={{ margin: 0 }}>
            The event rules above are all there is for this topic so far -- your coach will add study material soon.
          </p>
        </div>
      )}

      {available.length > 0 && (
        <>
          <div className="row" style={{ marginTop: assessment ? 24 : 0, marginBottom: 12 }}>
            {available.map((v) => (
              <button key={v.key} className={activeView === v.key ? "primary" : ""} onClick={() => setView(v.key)}>
                {v.label}
              </button>
            ))}
            {learningLive && concepts.length > 0 && (
              <Link to={`/student/${id}/present`}>
                <button>Watch presentation</button>
              </Link>
            )}
          </div>

          {activeView === "lesson" && chapterLesson && (
            <LessonReader lesson={chapterLesson} diagrams={diagrams} onZoom={setZoomed} />
          )}

          {activeView === "words" && chapterLesson && <WordBank lesson={chapterLesson} />}

          {activeView === "quiz" && chapterLesson && <QuickCheck lesson={chapterLesson} />}

          {activeView === "flashcards" && (
            <div className="study-cards">
              {concepts.map((c, i) => (
                <article className="study-card" key={c.id}>
                  <div className="study-card-head">
                    {c.image_data_url ? (
                      <img src={c.image_data_url} alt="" className="study-card-badge" />
                    ) : (
                      <span className="flashcard-monogram">{c.term.slice(0, 1).toUpperCase()}</span>
                    )}
                    <div>
                      <span className="study-card-count">
                        {i + 1} / {concepts.length}
                      </span>
                      <h3 className="study-card-term">{c.term}</h3>
                    </div>
                  </div>
                  {c.analogy && <p className="study-card-analogy">{c.analogy}</p>}
                  <p className="study-card-explanation">{c.explanation_md}</p>
                  {c.why_it_matters && (
                    <p className="study-card-why">
                      <strong>Why it matters:</strong> {c.why_it_matters}
                    </p>
                  )}
                  <span className={`tag ${c.video_relevant ? "video" : "general"}`} style={{ alignSelf: "flex-start" }}>
                    {sourceTag(c)}
                  </span>
                </article>
              ))}
            </div>
          )}

          {activeView === "story" && (
            <div className="card">
              <p className="story-content" style={{ whiteSpace: "pre-wrap", margin: 0 }}>
                {topic.story_md}
              </p>
            </div>
          )}

          {activeView === "notes" && (
            <div className="stack">
              {sourceNotes.map((r) => (
                <div className="card stack" key={r.id}>
                  <strong>{r.title}</strong>
                  {r.source_url && (
                    <a href={r.source_url} target="_blank" rel="noreferrer" className="muted">
                      {r.source_url}
                    </a>
                  )}
                  <p className="source-notes">{r.raw_text}</p>
                </div>
              ))}
            </div>
          )}
        </>
      )}

      {diagrams.length > 0 && !chapterLesson && (
        <>
          <h2 style={{ marginTop: 24 }}>Infographics &amp; diagrams</h2>
          <p className="muted">Tap one to see it full screen.</p>
          <div className="infographic-list">
            {diagrams.map((d) => (
              <div className="card diagram-card zoomable" key={d.id} onClick={() => setZoomed(d)} role="button" tabIndex={0}>
                <img src={d.image_data_url} alt={d.caption} />
                <p className="muted">{d.caption}</p>
              </div>
            ))}
          </div>
        </>
      )}

      {zoomed && (
        <div className="lightbox" onClick={() => setZoomed(null)} role="dialog" aria-label={zoomed.caption}>
          <img src={zoomed.image_data_url} alt={zoomed.caption} />
          <p>{zoomed.caption}</p>
          <span className="lightbox-hint">Tap anywhere or press Esc to close</span>
        </div>
      )}

      {hasLessons ? (
        <>
          <h2 style={{ marginTop: 24 }}>Ask a question</h2>
          <AskQuestions topicId={id} subject={parent?.name ?? topic.name} />
        </>
      ) : (
        <>
          <h2 style={{ marginTop: 24 }}>Ask about this content</h2>
          <TopicChat topicId={id} />
        </>
      )}
    </div>
  );
}
