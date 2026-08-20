const KEY = "so_session_token";

// One token per browser (not per topic) -- identifies an anonymous student
// across page reloads for resumable chat history, since this app has no
// student accounts (Attempt.student_name is just free text, no auth).
export function getOrCreateSessionToken(): string {
  let token = localStorage.getItem(KEY);
  if (!token) {
    token = crypto.randomUUID();
    localStorage.setItem(KEY, token);
  }
  return token;
}
