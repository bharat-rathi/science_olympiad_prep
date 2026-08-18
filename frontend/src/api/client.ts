// Relative -- in dev, Vite's proxy (see vite.config.ts) forwards /api to the
// local backend; in production the backend serves this built frontend itself,
// so API calls are same-origin. Either way, no hardcoded host/CORS to manage.
const BASE = "";

export interface Coach {
  id: number;
  // null for a coach who's been invited by email but hasn't signed in with
  // Google yet -- their profile name isn't known until they do.
  name: string | null;
}

export interface MeResponse {
  authenticated: boolean;
  coach: Coach | null;
  needs_bootstrap: boolean;
}

export interface Topic {
  id: number;
  event_name: string;
  name: string;
  description: string;
  created_at: string;
  created_by: string | null;
  content_published: boolean;
  story_md: string;
}

export interface Resource {
  id: number;
  topic_id: number;
  type: "video" | "text" | "link" | "pdf" | "research";
  title: string;
  source_url: string;
  status: string;
  created_at: string;
  raw_text: string;
  transcript: string;
}

export interface ConceptTerm {
  id: number;
  topic_id: number;
  term: string;
  explanation_md: string;
  analogy: string;
  source_resource_ids: number[];
  video_relevant: boolean;
  approved: boolean;
  image_data_url: string;
}

export interface Question {
  id: number;
  assessment_id: number;
  prompt: string;
  type: "mcq" | "short";
  choices: string[];
  correct_answer: string;
  explanation: string;
  order: number;
}

export interface Assessment {
  id: number;
  topic_id: number;
  status: "draft" | "published";
  questions: Question[];
  created_by: string | null;
}

export interface Attempt {
  id: number;
  assessment_id: number;
  student_name: string;
  started_at: string;
  submitted_at: string | null;
  score: number | null;
}

export interface AttemptAnswer {
  id: number;
  question_id: number;
  student_answer: string;
  is_correct: boolean | null;
  hints_used: number;
}

export interface AttemptResult {
  attempt: Attempt;
  answers: AttemptAnswer[];
}

export interface TutorMessage {
  id: number;
  role: "user" | "assistant";
  content: string;
  created_at: string;
}

async function req<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    const body = await res.text();
    // FastAPI error responses are {"detail": "..."} -- surface that message
    // directly when present, since it's already written to be shown to the
    // coach (e.g. link_fetch.py's ValueError messages).
    let detail: string | undefined;
    try {
      const parsed = JSON.parse(body);
      if (typeof parsed.detail === "string") detail = parsed.detail;
    } catch {
      // not JSON -- fall through to the raw form below
    }
    throw new Error(detail ?? `${res.status} ${res.statusText}: ${body}`);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  me: () => req<MeResponse>("/api/auth/me"),
  inviteCoach: (email: string) => req<Coach>("/api/auth/invite", { method: "POST", body: JSON.stringify({ email }) }),
  logout: () => req<{ ok: boolean }>("/api/auth/logout", { method: "POST" }),

  listTopics: () => req<Topic[]>("/api/topics"),
  getTopic: (id: number) => req<Topic>(`/api/topics/${id}`),
  createTopic: (payload: { event_name: string; name: string; description?: string }) =>
    req<Topic>("/api/topics", { method: "POST", body: JSON.stringify(payload) }),

  listResources: (topicId: number) => req<Resource[]>(`/api/topics/${topicId}/resources`),
  addTextResource: (topicId: number, payload: { title: string; text: string; source_url?: string }) =>
    req<Resource>(`/api/topics/${topicId}/resources/text`, { method: "POST", body: JSON.stringify(payload) }),
  addLinkResource: (topicId: number, url: string) =>
    req<Resource>(`/api/topics/${topicId}/resources/link`, { method: "POST", body: JSON.stringify({ url }) }),
  uploadMediaResource: async (topicId: number, file: File): Promise<Resource[]> => {
    // Large uploads occasionally die mid-transfer with a raw network error
    // (connection reset by a flaky wifi hop, a corporate/antivirus HTTPS
    // inspection proxy, etc.) rather than a clean HTTP response -- that
    // shows up as fetch() throwing instead of resolving. One silent retry
    // papers over a one-off transient drop; a second real failure surfaces
    // to the coach as before.
    const attempt = async () => {
      const form = new FormData();
      form.append("file", file);
      const res = await fetch(`${BASE}/api/topics/${topicId}/resources/upload`, { method: "POST", body: form });
      if (!res.ok) throw new Error(await res.text());
      return res.json();
    };
    try {
      return await attempt();
    } catch (err) {
      if (err instanceof TypeError) return await attempt();
      throw err;
    }
  },
  deleteResource: (topicId: number, resourceId: number) =>
    req<void>(`/api/topics/${topicId}/resources/${resourceId}`, { method: "DELETE" }),

  listConcepts: (topicId: number) => req<ConceptTerm[]>(`/api/topics/${topicId}/concepts`),
  generateExplanations: (topicId: number) =>
    req<ConceptTerm[]>(`/api/topics/${topicId}/generate-explanations`, { method: "POST" }),
  updateConcept: (
    topicId: number,
    conceptId: number,
    payload: Partial<Pick<ConceptTerm, "term" | "explanation_md" | "analogy" | "approved">>,
  ) => req<ConceptTerm>(`/api/topics/${topicId}/concepts/${conceptId}`, { method: "PATCH", body: JSON.stringify(payload) }),
  refineConcept: (topicId: number, conceptId: number, feedback: string) =>
    req<ConceptTerm>(`/api/topics/${topicId}/concepts/${conceptId}/refine`, {
      method: "POST",
      body: JSON.stringify({ feedback }),
    }),
  generateConceptImage: (topicId: number, conceptId: number) =>
    req<ConceptTerm>(`/api/topics/${topicId}/concepts/${conceptId}/generate-image`, { method: "POST" }),
  generateStory: (topicId: number) => req<Topic>(`/api/topics/${topicId}/generate-story`, { method: "POST" }),
  updateStory: (topicId: number, story_md: string) =>
    req<Topic>(`/api/topics/${topicId}/story`, { method: "PATCH", body: JSON.stringify({ story_md }) }),
  publishContent: (topicId: number) => req<Topic>(`/api/topics/${topicId}/publish-content`, { method: "POST" }),
  unpublishContent: (topicId: number) => req<Topic>(`/api/topics/${topicId}/unpublish-content`, { method: "POST" }),

  getOrCreateAssessment: (topicId: number) =>
    req<Assessment>(`/api/topics/${topicId}/assessment`, { method: "POST" }),
  getLatestAssessment: (topicId: number) => req<Assessment | null>(`/api/topics/${topicId}/assessment`),
  getAssessment: (id: number) => req<Assessment>(`/api/assessments/${id}`),
  generateQuestions: (assessmentId: number, numMcq: number, numShort: number) =>
    req<Assessment>(`/api/assessments/${assessmentId}/generate-questions`, {
      method: "POST",
      body: JSON.stringify({ num_mcq: numMcq, num_short: numShort }),
    }),
  addQuestion: (
    assessmentId: number,
    payload: { prompt: string; type: "mcq" | "short"; choices: string[]; correct_answer: string; explanation?: string },
  ) => req<Question>(`/api/assessments/${assessmentId}/questions`, { method: "POST", body: JSON.stringify(payload) }),
  publishAssessment: (id: number) => req<Assessment>(`/api/assessments/${id}/publish`, { method: "POST" }),
  updateQuestion: (assessmentId: number, questionId: number, payload: Partial<Question>) =>
    req<Question>(`/api/assessments/${assessmentId}/questions/${questionId}`, {
      method: "PATCH",
      body: JSON.stringify(payload),
    }),
  deleteQuestion: (assessmentId: number, questionId: number) =>
    req<{ ok: boolean }>(`/api/assessments/${assessmentId}/questions/${questionId}`, { method: "DELETE" }),

  startAttempt: (assessmentId: number, studentName: string) =>
    req<Attempt>(`/api/assessments/${assessmentId}/attempts`, {
      method: "POST",
      body: JSON.stringify({ student_name: studentName }),
    }),
  requestHint: (attemptId: number, questionId: number) =>
    req<{ hint: string }>(`/api/attempts/${attemptId}/hint`, {
      method: "POST",
      body: JSON.stringify({ attempt_id: attemptId, question_id: questionId }),
    }),
  submitAttempt: (attemptId: number, answers: { question_id: number; student_answer: string }[]) =>
    req<AttemptResult>(`/api/attempts/${attemptId}/submit`, { method: "POST", body: JSON.stringify({ answers }) }),
  getAttempt: (attemptId: number) => req<AttemptResult>(`/api/attempts/${attemptId}`),

  getTutorThread: (attemptId: number, questionId: number) =>
    req<TutorMessage[]>(`/api/attempts/${attemptId}/questions/${questionId}/tutor`),
  startTutorThread: (attemptId: number, questionId: number) =>
    req<TutorMessage>(`/api/attempts/${attemptId}/questions/${questionId}/tutor/start`, { method: "POST" }),
  tutorTurn: (attemptId: number, questionId: number, message: string) =>
    req<TutorMessage>(`/api/tutor/turn`, {
      method: "POST",
      body: JSON.stringify({ attempt_id: attemptId, question_id: questionId, message }),
    }),
};
