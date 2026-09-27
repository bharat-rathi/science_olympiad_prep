import { useEffect, useState } from "react";
import { NavLink, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import CoachTopicBuilder from "./pages/CoachTopicBuilder";
import CoachAssessment from "./pages/CoachAssessment";
import CoachSchedule from "./pages/CoachSchedule";
import CoachStudents from "./pages/CoachStudents";
import StudentPractice from "./pages/StudentPractice";
import StudentTest from "./pages/StudentTest";
import TopicPresentation from "./pages/TopicPresentation";
import AiSettings from "./pages/AiSettings";
import { api, Coach, Student } from "./api/client";

export default function App() {
  const [loading, setLoading] = useState(true);
  const [coach, setCoach] = useState<Coach | null>(null);
  const [student, setStudent] = useState<Student | null>(null);
  const [needsBootstrap, setNeedsBootstrap] = useState(false);

  function refreshAuth() {
    api
      .me()
      .then((res) => {
        setCoach(res.coach);
        setStudent(res.student);
        setNeedsBootstrap(res.needs_bootstrap);
      })
      .finally(() => setLoading(false));
  }

  useEffect(refreshAuth, []);

  async function logout() {
    await api.logout();
    setCoach(null);
    setStudent(null);
    refreshAuth();
  }

  if (loading) return null;

  // Every page requires identifying yourself now -- coach (Google) or
  // student (username+PIN, see routers/students.py) -- there's no more
  // anonymous browsing of topics.
  if (!coach && !student) {
    return <Login needsBootstrap={needsBootstrap} onStudentLogin={refreshAuth} />;
  }

  return (
    <AuthedApp coach={coach} student={student} logout={logout} refreshAuth={refreshAuth} />
  );
}

// A student who is logged in (just not as a coach) hitting a coach-only
// route sees this instead of being bounced back to Login -- they're already
// authenticated, just the wrong role.
function CoachOnly({ coach, children }: { coach: Coach | null; children: React.ReactNode }) {
  if (!coach) {
    return (
      <div className="auth-shell">
        <div className="auth-logo">🔒</div>
        <h1>Coaches only</h1>
        <p className="muted">This page is for coaches. Ask your coach if you think you should have access.</p>
      </div>
    );
  }
  return <>{children}</>;
}

function AuthedApp({
  coach,
  student,
  logout,
  refreshAuth,
}: {
  coach: Coach | null;
  student: Student | null;
  logout: () => void;
  refreshAuth: () => void;
}) {
  const identityName = coach ? coach.name || "Pending sign-in" : student?.name || "";

  return (
    <>
      <nav className="top-nav">
        <span className="brand">
          <span className="brand-mark">🧪</span> OlympiadPrep
        </span>
        <NavLink to="/" end>
          Home
        </NavLink>
        {coach && <NavLink to="/students">Students</NavLink>}
        {coach && <NavLink to="/settings">AI Settings</NavLink>}
        <span style={{ marginLeft: "auto" }} className="nav-user">
          <span className="avatar">{(identityName || "?").slice(0, 1).toUpperCase()}</span>
          <span className="muted">{identityName}</span>
          <button onClick={logout}>Logout</button>
        </span>
      </nav>
      <div className="app-shell">
        <Routes>
          <Route path="/" element={<Home coach={coach} onCoachAdded={refreshAuth} />} />
          <Route
            path="/coach/:topicId"
            element={
              <CoachOnly coach={coach}>
                <CoachTopicBuilder />
              </CoachOnly>
            }
          />
          <Route
            path="/coach/:topicId/assessment"
            element={
              <CoachOnly coach={coach}>
                <CoachAssessment />
              </CoachOnly>
            }
          />
          <Route
            path="/coach/:topicId/schedule"
            element={
              <CoachOnly coach={coach}>
                <CoachSchedule />
              </CoachOnly>
            }
          />
          <Route
            path="/students"
            element={
              <CoachOnly coach={coach}>
                <CoachStudents />
              </CoachOnly>
            }
          />
          <Route path="/student/:topicId" element={<StudentPractice />} />
          <Route path="/student/:topicId/present" element={<TopicPresentation />} />
          <Route path="/student/:topicId/test/:assessmentId" element={<StudentTest />} />
          <Route
            path="/settings"
            element={
              <CoachOnly coach={coach}>
                <AiSettings />
              </CoachOnly>
            }
          />
        </Routes>
      </div>
    </>
  );
}
