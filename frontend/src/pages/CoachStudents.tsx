import { useEffect, useState } from "react";
import { api, Student } from "../api/client";

function suggestUsername(name: string): string {
  return name
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9\s.-]/g, "")
    .replace(/\s+/g, ".")
    .slice(0, 64);
}

export default function CoachStudents() {
  const [students, setStudents] = useState<Student[]>([]);
  const [name, setName] = useState("");
  const [username, setUsername] = useState("");
  const [usernameEdited, setUsernameEdited] = useState(false);
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  // Most recently generated PIN, shown once until the coach adds/resets
  // another student -- there is no "show me the PIN again" endpoint.
  const [lastPin, setLastPin] = useState<{ username: string; pin: string } | null>(null);

  function refresh() {
    api.listStudents().then(setStudents);
  }

  useEffect(refresh, []);

  function onNameChange(value: string) {
    setName(value);
    if (!usernameEdited) setUsername(suggestUsername(value));
  }

  async function addStudent() {
    if (!name.trim() || !username.trim()) return;
    setBusy(true);
    setError("");
    try {
      const created = await api.addStudent(name.trim(), username.trim());
      setLastPin({ username: created.student.username, pin: created.pin });
      setName("");
      setUsername("");
      setUsernameEdited(false);
      refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  async function resetPin(student: Student) {
    const created = await api.resetStudentPin(student.id);
    setLastPin({ username: created.student.username, pin: created.pin });
  }

  return (
    <div>
      <div className="page-header">
        <h1>Students</h1>
        <p className="muted">
          A shared roster any coach can see and manage -- add a student here, then give them their
          username and PIN to sign in at the login page.
        </p>
      </div>

      <div className="card stack">
        <input placeholder="Student's name" value={name} onChange={(e) => onNameChange(e.target.value)} />
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => {
            setUsername(e.target.value);
            setUsernameEdited(true);
          }}
        />
        {error && <p style={{ color: "var(--danger)" }}>{error}</p>}
        <button className="primary" onClick={addStudent} disabled={busy}>
          {busy ? "Adding..." : "Add student"}
        </button>
      </div>

      {lastPin && (
        <div className="card" style={{ background: "var(--accent-soft)", borderColor: "transparent" }}>
          <p style={{ margin: 0 }}>
            <strong>{lastPin.username}</strong>'s PIN: <strong>{lastPin.pin}</strong>
          </p>
          <p className="muted" style={{ margin: "4px 0 0" }}>
            Share this with the student now -- it won't be shown again. Use "Reset PIN" below if it's lost.
          </p>
        </div>
      )}

      <div className="stack" style={{ marginTop: 16 }}>
        {students.map((s) => (
          <div className="card row" style={{ justifyContent: "space-between" }} key={s.id}>
            <span>
              <strong>{s.name}</strong> <span className="muted">@{s.username}</span>
            </span>
            <button onClick={() => resetPin(s)}>Reset PIN</button>
          </div>
        ))}
        {students.length === 0 && <p className="muted">No students yet -- add one above.</p>}
      </div>
    </div>
  );
}
