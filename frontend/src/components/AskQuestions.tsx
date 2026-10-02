import { useState } from "react";
import { Link } from "react-router-dom";
import { api, AskMatch, AskResponse } from "../api/client";

const KIND_LABEL: Record<AskMatch["kind"], string> = {
  lesson: "Lesson",
  word: "Word bank",
  card: "Flashcard",
  quick_check: "Quick check",
  fact: "Note-sheet fact",
  rules: "Event rules",
};

type Turn = AskResponse & { aiLoading?: boolean };

// Students' questions are answered from the deterministic lessons first
// (instant, no AI). Only if that isn't enough can they ask the AI tutor,
// which is grounded on the same lesson notes.
export default function AskQuestions({ topicId, subject }: { topicId: number; subject: string }) {
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [turns, setTurns] = useState<Turn[]>([]);

  async function ask() {
    const question = input.trim();
    if (!question || busy) return;
    setBusy(true);
    setError("");
    try {
      const res = await api.askLesson(topicId, question);
      setTurns((prev) => [res, ...prev]);
      setInput("");
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  async function askAi(index: number) {
    const turn = turns[index];
    setTurns((prev) => prev.map((t, i) => (i === index ? { ...t, aiLoading: true } : t)));
    try {
      const res = await api.askLesson(topicId, turn.question, true);
      setTurns((prev) => prev.map((t, i) => (i === index ? { ...t, aiLoading: false, ai_answer: res.ai_answer, ai_error: res.ai_error } : t)));
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      setTurns((prev) => prev.map((t, i) => (i === index ? { ...t, aiLoading: false, ai_error: msg } : t)));
    }
  }

  return (
    <div className="card ask-box">
      <p className="muted" style={{ margin: "0 0 10px" }}>
        Ask anything about {subject}. We'll look through all your lessons first. If they don't answer it, you can ask the AI tutor.
      </p>
      <div className="row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && ask()}
          placeholder="e.g. Why is Venus hotter than Mercury?"
          disabled={busy}
          maxLength={500}
        />
        <button className="primary" onClick={ask} disabled={busy || !input.trim()}>
          {busy ? "Searching..." : "Ask"}
        </button>
      </div>
      {error && <p className="error">{error}</p>}

      {turns.map((turn, i) => (
        <div className="ask-turn" key={`${turns.length - i}`}>
          <div className="chat-bubble user">{turn.question}</div>
          {turn.matches.length > 0 ? (
            <>
              <span className="ask-label">From your lessons</span>
              {turn.matches.map((m, k) => (
                <div className="ask-match" key={k}>
                  <div className="ask-match-head">
                    <span className="tag general">{KIND_LABEL[m.kind]}</span>
                    {m.topic_id === topicId ? (
                      <span className="muted">{m.chapter}</span>
                    ) : (
                      <Link to={`/student/${m.topic_id}`} className="muted">
                        {m.chapter} &rarr;
                      </Link>
                    )}
                  </div>
                  {m.kind === "lesson" && <strong>{m.title}</strong>}
                  <p className="ask-match-text">{m.text}</p>
                </div>
              ))}
            </>
          ) : (
            <p className="muted">Your lessons don't seem to cover this one.</p>
          )}
          {turn.ai_answer ? (
            <div className="ask-ai">
              <span className="ask-label">AI tutor</span>
              <p style={{ whiteSpace: "pre-wrap", margin: "4px 0" }}>{turn.ai_answer}</p>
              <p className="muted" style={{ margin: 0, fontSize: 13 }}>
                AI answers can be wrong -- if it disagrees with your lessons, trust the lessons and ask your coach.
              </p>
            </div>
          ) : (
            <div className="row" style={{ marginTop: 8 }}>
              <button onClick={() => askAi(i)} disabled={turn.aiLoading}>
                {turn.aiLoading ? "Asking the AI tutor..." : turn.matches.length ? "Still confused? Ask the AI tutor" : "Ask the AI tutor"}
              </button>
              {turn.ai_error && <span className="error">{turn.ai_error}</span>}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
