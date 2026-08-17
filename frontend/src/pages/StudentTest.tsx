import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api, Assessment, Attempt, AttemptAnswer, TutorMessage } from "../api/client";

export default function StudentTest() {
  const { topicId, assessmentId } = useParams();
  const aid = Number(assessmentId);

  const [assessment, setAssessment] = useState<Assessment | null>(null);
  const [studentName, setStudentName] = useState("");
  const [attempt, setAttempt] = useState<Attempt | null>(null);
  const [answers, setAnswers] = useState<Record<number, string>>({});
  const [hints, setHints] = useState<Record<number, string[]>>({});
  const [results, setResults] = useState<AttemptAnswer[] | null>(null);
  const [openTutorFor, setOpenTutorFor] = useState<number | null>(null);
  const [threads, setThreads] = useState<Record<number, TutorMessage[]>>({});
  const [tutorInput, setTutorInput] = useState("");
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    api.getAssessment(aid).then(setAssessment);
  }, [aid]);

  async function start() {
    if (!studentName.trim()) return;
    const a = await api.startAttempt(aid, studentName);
    setAttempt(a);
  }

  async function getHint(questionId: number) {
    if (!attempt) return;
    const { hint } = await api.requestHint(attempt.id, questionId);
    setHints((prev) => ({ ...prev, [questionId]: [...(prev[questionId] || []), hint] }));
  }

  async function submit() {
    if (!attempt || !assessment) return;
    setBusy(true);
    try {
      const payload = assessment.questions.map((q) => ({ question_id: q.id, student_answer: answers[q.id] || "" }));
      const result = await api.submitAttempt(attempt.id, payload);
      setResults(result.answers);
    } finally {
      setBusy(false);
    }
  }

  async function openTutor(questionId: number) {
    if (!attempt) return;
    setOpenTutorFor(questionId);
    if (!threads[questionId]) {
      let thread = await api.getTutorThread(attempt.id, questionId);
      if (thread.length === 0) {
        const opening = await api.startTutorThread(attempt.id, questionId);
        thread = [opening];
      }
      setThreads((prev) => ({ ...prev, [questionId]: thread }));
    }
  }

  async function sendTutorMessage(questionId: number) {
    if (!attempt || !tutorInput.trim()) return;
    const userMsg: TutorMessage = { id: -1, role: "user", content: tutorInput, created_at: "" };
    setThreads((prev) => ({ ...prev, [questionId]: [...(prev[questionId] || []), userMsg] }));
    const text = tutorInput;
    setTutorInput("");
    const reply = await api.tutorTurn(attempt.id, questionId, text);
    setThreads((prev) => ({ ...prev, [questionId]: [...(prev[questionId] || []), reply] }));
  }

  if (!assessment) return <p>Loading...</p>;

  if (!attempt) {
    return (
      <div className="auth-shell">
        <div className="auth-logo">📝</div>
        <h1>{assessment.status === "published" ? "Ready to start" : "This test is not published yet"}</h1>
        <div className="card stack" style={{ marginTop: 20, textAlign: "left" }}>
          <input placeholder="Your name" value={studentName} onChange={(e) => setStudentName(e.target.value)} />
          <button className="primary" onClick={start} disabled={assessment.status !== "published"}>
            Start test
          </button>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="page-header">
        <h1>Test in progress</h1>
      </div>
      <div className="stack">
        {assessment.questions.map((q) => {
          const result = results?.find((r) => r.question_id === q.id);
          return (
            <div className="card accent-top" key={q.id}>
              <p className="card-title" style={{ margin: "0 0 12px" }}>
                {q.prompt}
              </p>

              {q.type === "mcq" ? (
                <div className="stack">
                  {q.choices.map((c) => (
                    <label key={c} className="row">
                      <input
                        type="radio"
                        name={`q-${q.id}`}
                        checked={answers[q.id] === c}
                        disabled={!!results}
                        onChange={() => setAnswers((prev) => ({ ...prev, [q.id]: c }))}
                      />
                      {c}
                    </label>
                  ))}
                </div>
              ) : (
                <input
                  value={answers[q.id] || ""}
                  disabled={!!results}
                  onChange={(e) => setAnswers((prev) => ({ ...prev, [q.id]: e.target.value }))}
                />
              )}

              {!results && (
                <div className="row">
                  <button onClick={() => getHint(q.id)}>Hint</button>
                </div>
              )}
              {hints[q.id]?.map((h, i) => (
                <p key={i} className="muted">
                  💡 {h}
                </p>
              ))}

              {result && (
                <div className="stack">
                  <span className={result.is_correct ? "correct" : "incorrect"}>
                    {result.is_correct ? "Correct" : "Incorrect"}
                  </span>
                  <p className="muted">{q.explanation}</p>
                  {!result.is_correct && (
                    <button onClick={() => openTutor(q.id)}>{openTutorFor === q.id ? "Tutor chat open" : "Talk to a tutor"}</button>
                  )}
                  {openTutorFor === q.id && (
                    <div className="card">
                      <div className="chat-thread">
                        {(threads[q.id] || []).map((m, i) => (
                          <div key={i} className={`chat-bubble ${m.role}`}>
                            {m.content}
                          </div>
                        ))}
                      </div>
                      <div className="row">
                        <input
                          value={tutorInput}
                          onChange={(e) => setTutorInput(e.target.value)}
                          onKeyDown={(e) => e.key === "Enter" && sendTutorMessage(q.id)}
                          placeholder="Type your response..."
                        />
                        <button className="primary" onClick={() => sendTutorMessage(q.id)}>
                          Send
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {!results && (
        <button className="primary" onClick={submit} disabled={busy}>
          {busy ? "Grading..." : "Submit test"}
        </button>
      )}
    </div>
  );
}
