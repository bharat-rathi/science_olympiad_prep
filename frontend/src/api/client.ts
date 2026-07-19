const BASE = "http://localhost:8000";

export interface Topic {
  id: number;
  event_name: string;
  name: string;
  description: string;
  created_at: string;
}

export interface Resource {
  id: number;
  topic_id: number;
  type: "video" | "text" | "link";
  title: string;
  source_url: string;
  status: string;
  created_at: string;
}

export interface ConceptTerm {
  id: number;
  topic_id: number;
  term: string;
  explanation_md: string;
  source_resource_ids: number[];
  video_relevant: boolean;
  approved: boolean;
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
    throw new Error(`${res.status} ${res.statusText}: ${body}`);
  }
  if (res.status === 204) return undefined as T;
  return res.json();
}

export const api = {
  listTopics: () => req<Topic[]>("/api/topics"),
  getTopic: (id: number) => req<Topic>(`/api/topics/${id}`),
  createTopic: (payload: { event_name: string; name: string; description?: string }) =>
    req<Topic>("/api/topics", { method: "POST", body: JSON.stringify(payload) }),

  listResources: (topicId: number) => req<Resource[]>(`/api/topics/${topicId}/resources`),
  addTextResource: (topicId: number, payload: { title: string; text: string; source_url?: string }) =>
    req<Resource>(`/api/topics/${topicId}/resources/text`, { method: "POST", body: JSON.stringify(payload) }),
  uploadMediaResource: async (topicId: number, file: File): Promise<Resource[]> => {
    const form = new FormData();
    form.append("file", file);
    const res = await fetch(`${BASE}/api/topics/${topicId}/resources/upload`, { method: "POST", body: form });
    if (!res.ok) throw new Error(await res.text());
    return res.json();
  },

  listConcepts: (topicId: number) => req<ConceptTerm[]>(`/api/topics/${topicId}/concepts`),
  generateExplanations: (topicId: number) =>
    req<ConceptTerm[]>(`/api/topics/${topicId}/generate-explanations`, { method: "POST" }),
  updateConcept: (topicId: number, conceptId: number, payload: Partial<Pick<ConceptTerm, "term" | "explanation_md" | "approved">>) =>
    req<ConceptTerm>(`/api/topics/${topicId}/concepts/${conceptId}`, { method: "PATCH", body: JSON.stringify(payload) }),

  generateAssessment: (topicId: number) =>
    req<Assessment>(`/api/topics/${topicId}/assessment/generate`, { method: "POST" }),
  getLatestAssessment: (topicId: number) => req<Assessment | null>(`/api/topics/${topicId}/assessment`),
  getAssessment: (id: number) => req<Assessment>(`/api/assessments/${id}`),
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
