import { useEffect, useState } from "react";
import { Link, NavLink, Route, Routes } from "react-router-dom";
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

  // The landing page is the student view, open without signing in; coaches
  // reach their side through the Coach button (top left), which asks them to
  // sign in first. Students can still sign in to see topics assigned to them.
  return (
    <AuthedApp
      coach={coach}
      student={student}
      needsBootstrap={needsBootstrap}
      logout={logout}
      refreshAuth={refreshAuth}
    />
  );
}

// Coach-only routes: a visitor who isn't signed in gets the sign-in page; a
// signed-in student sees this instead -- authenticated, just the wrong role.
function CoachOnly({
  coach,
  student,
  needsBootstrap,
  children,
}: {
  coach: Coach | null;
  student: Student | null;
  needsBootstrap: boolean;
  children: React.ReactNode;
}) {
  if (!coach && !student) return <Login needsBootstrap={needsBootstrap} />;
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
  needsBootstrap,
  logout,
  refreshAuth,
}: {
  coach: Coach | null;
  student: Student | null;
  needsBootstrap: boolean;
  logout: () => void;
  refreshAuth: () => void;
}) {
  const identityName = coach ? coach.name || "Pending sign-in" : student?.name || "";
  const guard = (page: React.ReactNode) => (
    <CoachOnly coach={coach} student={student} needsBootstrap={needsBootstrap}>
      {page}
    </CoachOnly>
  );

  return (
    <>
      <nav className="top-nav">
        <NavLink to="/coach" className="coach-button">
          Coach
        </NavLink>
        <Link to="/" className="brand">
          <span className="brand-mark">🧪</span> OlympiadPrep
        </Link>
        <NavLink to="/" end>
          Events
        </NavLink>
        {coach && <NavLink to="/students">Students</NavLink>}
        {coach && <NavLink to="/settings">AI Settings</NavLink>}
        <span style={{ marginLeft: "auto" }} className="nav-user">
          {coach || student ? (
            <>
              <span className="avatar">{(identityName || "?").slice(0, 1).toUpperCase()}</span>
              <span className="muted nav-user-name">{identityName}</span>
              <button onClick={logout}>Logout</button>
            </>
          ) : (
            <a href="/api/auth/google/login">
              <button>Student sign in</button>
            </a>
          )}
        </span>
      </nav>
      <div className="app-shell">
        <Routes>
          <Route path="/" element={<Home coach={null} onCoachAdded={refreshAuth} />} />
          <Route path="/coach" element={guard(<Home coach={coach} onCoachAdded={refreshAuth} />)} />
          <Route
            path="/coach/:topicId"
            element={guard(<CoachTopicBuilder />)}
          />
          <Route
            path="/coach/:topicId/assessment"
            element={guard(<CoachAssessment />)}
          />
          <Route
            path="/coach/:topicId/schedule"
            element={guard(<CoachSchedule />)}
          />
          <Route
            path="/students"
            element={guard(<CoachStudents />)}
          />
          <Route path="/student/:topicId" element={<StudentPractice />} />
          <Route path="/student/:topicId/present" element={<TopicPresentation />} />
          <Route path="/student/:topicId/test/:assessmentId" element={<StudentTest />} />
          <Route
            path="/settings"
            element={guard(<AiSettings />)}
          />
        </Routes>
      </div>
    </>
  );
}
