import { useState } from "react";
import { api } from "../api/client";

export default function Login({ needsBootstrap, onAuthed }: { needsBootstrap: boolean; onAuthed: () => void }) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setBusy(true);
    setError("");
    try {
      if (needsBootstrap) {
        await api.register(name.trim(), password);
      } else {
        await api.login(name.trim(), password);
      }
      onAuthed();
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="app-shell" style={{ maxWidth: 380, marginTop: 60 }}>
      <h1>🧪 Science Olympiad Coach</h1>
      {needsBootstrap ? (
        <p className="muted">
          No coach accounts exist yet -- create the first one. You'll be logged in immediately, and
          can add teammates from the home page afterward.
        </p>
      ) : (
        <p className="muted">Log in with your coach account.</p>
      )}
      <form className="card stack" onSubmit={submit}>
        <input placeholder="Your name" value={name} onChange={(e) => setName(e.target.value)} required />
        <input
          type="password"
          placeholder={needsBootstrap ? "Choose a password (8+ characters)" : "Password"}
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        {error && <p style={{ color: "var(--danger)" }}>{error}</p>}
        <button className="primary" type="submit" disabled={busy}>
          {busy ? "Working..." : needsBootstrap ? "Create account & log in" : "Log in"}
        </button>
      </form>
    </div>
  );
}
