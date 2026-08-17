export default function Login({ needsBootstrap }: { needsBootstrap: boolean }) {
  const notInvited = new URLSearchParams(window.location.search).get("error") === "not_invited";

  return (
    <div className="auth-shell">
      <div className="auth-logo">🧪</div>
      <h1>Empower Your Future Scientists</h1>
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
          <button className="google pill">
            <svg width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">
              <path
                fill="#4285F4"
                d="M17.64 9.2c0-.64-.06-1.25-.16-1.84H9v3.48h4.84a4.14 4.14 0 0 1-1.8 2.72v2.26h2.9c1.7-1.57 2.7-3.88 2.7-6.62z"
              />
              <path
                fill="#34A853"
                d="M9 18c2.43 0 4.47-.8 5.96-2.18l-2.9-2.26c-.8.54-1.84.86-3.06.86-2.35 0-4.34-1.59-5.05-3.72H.9v2.33A9 9 0 0 0 9 18z"
              />
              <path
                fill="#FBBC05"
                d="M3.95 10.7A5.4 5.4 0 0 1 3.67 9c0-.59.1-1.17.28-1.7V4.97H.9A9 9 0 0 0 0 9c0 1.45.35 2.83.9 4.03l3.05-2.33z"
              />
              <path
                fill="#EA4335"
                d="M9 3.58c1.32 0 2.5.46 3.44 1.35l2.58-2.58C13.46.89 11.43 0 9 0A9 9 0 0 0 .9 4.97L3.95 7.3C4.66 5.17 6.65 3.58 9 3.58z"
              />
            </svg>
            Sign in with Google
          </button>
        </a>
      </div>
    </div>
  );
}
