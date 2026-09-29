import { useEffect, useState } from "react";
import { api, Student, Topic } from "../api/client";

export default function CoachStudents() {
  const [students, setStudents] = useState<Student[]>([]);
  const [topics, setTopics] = useState<Topic[]>([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const [openTopicsFor, setOpenTopicsFor] = useState<number | null>(null);

  function refresh() {
    api.listStudents().then(setStudents);
    api.listTopics(true).then(setTopics);
  }

  useEffect(refresh, []);

  async function addStudent() {
    if (!name.trim() || !email.trim()) return;
    setBusy(true);
    setError("");
    try {
      const created = await api.addStudent(name.trim(), email.trim());
      setStudents((prev) => [...prev, created]);
      setName("");
      setEmail("");
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  async function toggleTopic(student: Student, topicId: number) {
    const has = student.topic_ids.includes(topicId);
    const nextIds = has ? student.topic_ids.filter((id) => id !== topicId) : [...student.topic_ids, topicId];
    const updated = await api.setStudentTopics(student.id, nextIds);
    setStudents((prev) => prev.map((s) => (s.id === student.id ? updated : s)));
  }

  return (
    <div>
      <div className="page-header">
        <h1>Students</h1>
        <p className="muted">
          A shared roster any coach can see and manage -- add a student by their Google account
          email, then choose which topics they can see. They sign in with the same "Sign in with
          Google" button as coaches, using that email.
        </p>
      </div>

      <div className="card stack">
        <input placeholder="Student's name" value={name} onChange={(e) => setName(e.target.value)} />
        <input
          type="email"
          placeholder="Student's Google account email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        {error && <p style={{ color: "var(--danger)" }}>{error}</p>}
        <button className="primary" onClick={addStudent} disabled={busy}>
          {busy ? "Adding..." : "Add student"}
        </button>
      </div>

      <div className="stack" style={{ marginTop: 16 }}>
        {students.map((s) => (
          <div className="card stack" key={s.id}>
            <div className="row" style={{ justifyContent: "space-between" }}>
              <span>
                <strong>{s.name}</strong> <span className="muted">{s.email}</span>
              </span>
              <button onClick={() => setOpenTopicsFor(openTopicsFor === s.id ? null : s.id)}>
                {openTopicsFor === s.id ? "Done" : `Topics (${s.topic_ids.length})`}
              </button>
            </div>
            {openTopicsFor === s.id && (
              <div className="stack" style={{ paddingLeft: 8 }}>
                <p className="muted" style={{ margin: 0 }}>
                  {s.name} can only see the topics checked here.
                </p>
                {topics.map((t) => (
                  <label key={t.id} className="row">
                    <input
                      type="checkbox"
                      checked={s.topic_ids.includes(t.id)}
                      onChange={() => toggleTopic(s, t.id)}
                    />
                    {t.name}
                  </label>
                ))}
                {topics.length === 0 && <p className="muted">No topics exist yet.</p>}
              </div>
            )}
          </div>
        ))}
        {students.length === 0 && <p className="muted">No students yet -- add one above.</p>}
      </div>
    </div>
  );
}
