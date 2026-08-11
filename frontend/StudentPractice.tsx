import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, Assessment, ConceptTerm, Topic } from "../api/client";

export default function StudentPractice() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [view, setView] = useState<"flashcards" | "story">("flashcards");
  const [flipped, setFlipped] = useState<Set<number>>(new Set());
  const [expanded, setExpanded] = useState<Set<number>>(new Set());

  useEffect(() => {
    api.getTopic(id).then(setTopic);
    api.listConcepts(id).then((all) => setConcepts(all.filter((c) => c.approved)));
    // Assessment visibility is independent of the topic's learning-content
    // publish flag -- a coach can publish a test without (or before)
    // publishing the concepts/story, and vice versa.
    api.getLatestAssessment(id).then((a) => setAssessment(a && a.status === "published" ? a : null));
  }, [id]);

  function toggleFlip(conceptId: number) {
    setFlipped((prev) => {
      const next = new Set(prev);
      if (next.has(conceptId)) next.delete(conceptId);
      else next.add(conceptId);
      return next;
    });
  }

  function toggleExpand(e: React.MouseEvent, conceptId: number) {
    e.stopPropagation();
    setExpanded((prev) => {
      const next = new Set(prev);
      if (next.has(conceptId)) next.delete(conceptId);
      else next.add(conceptId);
      return next;
    });
  }

  if (!topic) return <p>Loading...</p>;

  return (
    <div>
      <div className="page-header">
        <h1>{topic.name}</h1>
        <p className="muted">{topic.description}</p>
      </div>

      {assessment && (
        <div className="card row" style={{ justifyContent: "space-between" }}>
          <span>A practice test is ready for this topic.</span>
          <Link to={`/student/${id}/test/${assessment.id}`}>
            <button className="primary">Start test</button>
          </Link>
        </div>
      )}

      {!topic.content_published ? (
        <div className="card">
          <p className="muted" style={{ margin: 0 }}>
            Your coach hasn't published the learning material for this topic yet -- check back soon.
          </p>
        </div>
      ) : (
        <>
          <div className="row" style={{ marginTop: assessment ? 24 : 0, marginBottom: 4 }}>
            <button className={view === "flashcards" ? "primary" : ""} onClick={() => setView("flashcards")}>
              Flashcards
            </button>
            {topic.story_md && (
              <button className={view === "story" ? "primary" : ""} onClick={() => setView("story")}>
                Story
              </button>
            )}
          </div>

          {view === "flashcards" ? (
            <>
              <p className="muted">Tap a card to flip it.</p>
              <div className="grid-2">
                {concepts.map((c, i) => {
                  const isFlipped = flipped.has(c.id);
                  const isExpanded = expanded.has(c.id);
                  return (
                    <div
                      className={`flashcard ${isFlipped ? "flipped" : ""}`}
                      key={c.id}
                      onClick={() => toggleFlip(c.id)}
                      role="button"
                      tabIndex={0}
                    >
                      <div className="flashcard-inner">
                        <div className="flashcard-face flashcard-front">
                          <span className="flashcard-count">
                            {i + 1} / {concepts.length}
                          </span>
                          {c.image_data_url ? (
                            <img src={c.image_data_url} alt={c.term} className="flashcard-image" />
                          ) : (
                            <span className="flashcard-monogram">{c.term.slice(0, 1).toUpperCase()}</span>
                          )}
                          <strong>{c.term}</strong>
                          <span className="muted" style={{ marginTop: 8 }}>
                            Tap to reveal
                          </span>
                        </div>
                        <div className="flashcard-face flashcard-back">
                          {c.analogy ? (
                            <>
                              <p className="flashcard-analogy">{c.analogy}</p>
                              <button className="flashcard-expand-toggle" onClick={(e) => toggleExpand(e, c.id)}>
                                {isExpanded ? "Hide full explanation" : "Show full explanation"}
                              </button>
                              {isExpanded && <p className="muted flashcard-explanation">{c.explanation_md}</p>}
                            </>
                          ) : (
                            <p className="flashcard-explanation" style={{ margin: 0 }}>
                              {c.explanation_md}
                            </p>
                          )}
                          <span className={`tag ${c.video_relevant ? "video" : "general"}`} style={{ marginTop: "auto" }}>
                            {c.video_relevant ? "from team video" : c.source_resource_ids.length ? "from team resource" : "general knowledge"}
                          </span>
                        </div>
                      </div>
                    </div>
                  );
                })}
                {concepts.length === 0 && <p className="muted">Your coach hasn't approved any concepts for this topic yet.</p>}
              </div>
            </>
          ) : (
            <div className="card">
              <p style={{ whiteSpace: "pre-wrap", margin: 0, lineHeight: 1.7 }}>{topic.story_md}</p>
            </div>
          )}
        </>
      )}
    </div>
  );
}
