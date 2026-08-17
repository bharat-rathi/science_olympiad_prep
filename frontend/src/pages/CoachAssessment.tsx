import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, Assessment, Question } from "../api/client";

const EMPTY_MCQ_CHOICES = ["", "", "", ""];

export default function CoachAssessment() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const [numMcq, setNumMcq] = useState(4);
  const [numShort, setNumShort] = useState(2);

  const [showManual, setShowManual] = useState(false);
  const [manualType, setManualType] = useState<"mcq" | "short">("mcq");
  const [manualPrompt, setManualPrompt] = useState("");
  const [manualChoices, setManualChoices] = useState<string[]>(EMPTY_MCQ_CHOICES);
  const [manualCorrect, setManualCorrect] = useState("");
  const [manualExplanation, setManualExplanation] = useState("");

  useEffect(() => {
    api.getOrCreateAssessment(id).then(setAssessment);
  }, [id]);

  async function generateMore() {
    if (!assessment) return;
    setBusy(true);
    setError("");
    try {
      const a = await api.generateQuestions(assessment.id, numMcq, numShort);
      setAssessment(a);
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  async function addManualQuestion() {
    if (!assessment || !manualPrompt.trim() || !manualCorrect.trim()) return;
    setError("");
    try {
      await api.addQuestion(assessment.id, {
        prompt: manualPrompt,
        type: manualType,
        choices: manualType === "mcq" ? manualChoices.filter((c) => c.trim()) : [],
        correct_answer: manualCorrect,
        explanation: manualExplanation,
      });
      const refreshed = await api.getAssessment(assessment.id);
      setAssessment(refreshed);
      setManualPrompt("");
      setManualChoices(EMPTY_MCQ_CHOICES);
      setManualCorrect("");
      setManualExplanation("");
      setShowManual(false);
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
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

  if (!assessment) return <p>Loading...</p>;

  return (
    <div>
      <div className="page-header">
        <h1>Assessment editor</h1>
      </div>
      {error && <p style={{ color: "var(--danger)" }}>{error}</p>}

      <div className="row" style={{ justifyContent: "space-between" }}>
        <span className={`tag ${assessment.status === "published" ? "success" : "general"}`}>{assessment.status}</span>
        <div className="row">
          {assessment.status === "draft" && (
            <button className="primary" onClick={publish} disabled={assessment.questions.length === 0}>
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

      <h2>Suggest questions</h2>
      <p className="muted">The system suggests questions grounded in your approved concepts -- you pick how many of each type, then edit or remove any of them below.</p>
      <div className="card row">
        <label>
          MCQ
          <input type="number" min={0} max={20} value={numMcq} onChange={(e) => setNumMcq(Number(e.target.value))} style={{ width: 60, marginLeft: 6 }} />
        </label>
        <label>
          Short answer
          <input type="number" min={0} max={20} value={numShort} onChange={(e) => setNumShort(Number(e.target.value))} style={{ width: 60, marginLeft: 6 }} />
        </label>
        <button className="accent" onClick={generateMore} disabled={busy}>
          {busy ? "Generating..." : "✨ Generate"}
        </button>
      </div>

      <h2>Add your own question</h2>
      {showManual ? (
        <div className="card stack">
          <div className="row">
            <label>
              <input type="radio" checked={manualType === "mcq"} onChange={() => setManualType("mcq")} /> Multiple choice
            </label>
            <label>
              <input type="radio" checked={manualType === "short"} onChange={() => setManualType("short")} /> Short answer
            </label>
          </div>
          <textarea placeholder="Question prompt" value={manualPrompt} onChange={(e) => setManualPrompt(e.target.value)} />
          {manualType === "mcq" && (
            <div className="stack">
              {manualChoices.map((c, i) => (
                <input
                  key={i}
                  placeholder={`Choice ${i + 1}`}
                  value={c}
                  onChange={(e) => {
                    const next = [...manualChoices];
                    next[i] = e.target.value;
                    setManualChoices(next);
                  }}
                />
              ))}
            </div>
          )}
          <input placeholder="Correct answer" value={manualCorrect} onChange={(e) => setManualCorrect(e.target.value)} />
          <textarea
            placeholder="Explanation (shown after answering, optional)"
            value={manualExplanation}
            onChange={(e) => setManualExplanation(e.target.value)}
          />
          <div className="row">
            <button className="primary" onClick={addManualQuestion}>
              Add question
            </button>
            <button onClick={() => setShowManual(false)}>Cancel</button>
          </div>
        </div>
      ) : (
        <button onClick={() => setShowManual(true)}>+ Add a question manually</button>
      )}

      <h2>Questions ({assessment.questions.length})</h2>
      <div className="stack" style={{ marginTop: 12 }}>
        {assessment.questions.map((q) => (
          <div className="card accent-top" key={q.id}>
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
    </div>
  );
}
