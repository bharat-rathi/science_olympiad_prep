export default function Login({ needsBootstrap }: { needsBootstrap: boolean }) {
  const notInvited = new URLSearchParams(window.location.search).get("error") === "not_invited";

  return (
    <div className="auth-shell">
      <div className="auth-logo">🧪</div>
      <h1>Science Olympiad Coach</h1>
      {needsBootstrap ? (
        <p className="muted">
          No coach accounts exist yet -- sign in with Google to create the first one. You'll be
          logged in immediately, and can invite teammates by email from the home page afterward.
        </p>
      ) : (
        <p className="muted">Coaches sign in with the Google account they were invited with.</p>
      )}
      {notInvited && (
        <div className="card" style={{ background: "var(--danger-soft)", borderColor: "transparent" }}>
          <p style={{ color: "var(--danger)", margin: 0 }}>
            That Google account hasn't been invited yet -- ask an existing coach to add your email
            from the home page, then try again.
          </p>
        </div>
      )}
      <div className="card" style={{ marginTop: 20 }}>
        <a href="/api/auth/google/login">
          <button className="primary" style={{ width: "100%" }}>
            Sign in with Google
          </button>
        </a>
      </div>
    </div>
  );
}
