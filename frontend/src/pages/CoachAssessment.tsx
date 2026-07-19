import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, Assessment, Question } from "../api/client";

export default function CoachAssessment() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  function refresh() {
    api.getLatestAssessment(id).then(setAssessment);
  }

  useEffect(refresh, [id]);

  async function generate() {
    setBusy(true);
    setError("");
    try {
      const a = await api.generateAssessment(id);
      setAssessment(a);
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
    }
  }

  async function updateQuestion(q: Question, patch: Partial<Question>) {
    if (!assessment) return;
    const updated = await api.updateQuestion(assessment.id, q.id, patch);
    setAssessment({ ...assessment, questions: assessment.questions.map((x) => (x.id === q.id ? updated : x)) });
  }

  async function deleteQuestion(q: Question) {
    if (!assessment) return;
    await api.deleteQuestion(assessment.id, q.id);
    setAssessment({ ...assessment, questions: assessment.questions.filter((x) => x.id !== q.id) });
  }

  async function publish() {
    if (!assessment) return;
    const updated = await api.publishAssessment(assessment.id);
    setAssessment(updated);
  }

  return (
    <div>
      <h1>Assessment editor</h1>
      {error && <p style={{ color: "var(--danger)" }}>{error}</p>}

      {!assessment && (
        <button className="primary" onClick={generate} disabled={busy}>
          {busy ? "Generating..." : "Generate assessment from approved concepts"}
        </button>
      )}

      {assessment && (
        <>
          <div className="row" style={{ justifyContent: "space-between" }}>
            <span className="tag">{assessment.status}</span>
            <div className="row">
              <button onClick={generate} disabled={busy}>
                {busy ? "Working..." : "Regenerate"}
              </button>
              {assessment.status === "draft" && (
                <button className="primary" onClick={publish}>
                  Publish
                </button>
              )}
              {assessment.status === "published" && (
                <Link to={`/student/${id}/test/${assessment.id}`}>
                  <button className="primary">Open student test</button>
                </Link>
              )}
            </div>
          </div>

          <div className="stack" style={{ marginTop: 12 }}>
            {assessment.questions.map((q) => (
              <div className="card" key={q.id}>
                <div className="row" style={{ justifyContent: "space-between" }}>
                  <span className="tag">{q.type}</span>
                  <button onClick={() => deleteQuestion(q)}>Remove</button>
                </div>
                <textarea defaultValue={q.prompt} onBlur={(e) => e.target.value !== q.prompt && updateQuestion(q, { prompt: e.target.value })} />
                {q.type === "mcq" && (
                  <div className="stack">
                    {q.choices.map((c, i) => (
                      <input
                        key={i}
                        defaultValue={c}
                        onBlur={(e) => {
                          if (e.target.value === c) return;
                          const choices = [...q.choices];
                          choices[i] = e.target.value;
                          updateQuestion(q, { choices });
                        }}
                      />
                    ))}
                  </div>
                )}
                <label className="muted">Correct answer</label>
                <input
                  defaultValue={q.correct_answer}
                  onBlur={(e) => e.target.value !== q.correct_answer && updateQuestion(q, { correct_answer: e.target.value })}
                />
                <label className="muted">Explanation (shown after answering)</label>
                <textarea
                  defaultValue={q.explanation}
                  onBlur={(e) => e.target.value !== q.explanation && updateQuestion(q, { explanation: e.target.value })}
                />
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
