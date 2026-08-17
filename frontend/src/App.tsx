import { useEffect, useState } from "react";
import { NavLink, Route, Routes, useLocation } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import CoachTopicBuilder from "./pages/CoachTopicBuilder";
import CoachAssessment from "./pages/CoachAssessment";
import StudentPractice from "./pages/StudentPractice";
import StudentTest from "./pages/StudentTest";
import { api, Coach } from "./api/client";

export default function App() {
  const [loading, setLoading] = useState(true);
  const [coach, setCoach] = useState<Coach | null>(null);
  const [needsBootstrap, setNeedsBootstrap] = useState(false);

  function refreshAuth() {
    api
      .me()
      .then((res) => {
        setCoach(res.coach);
        setNeedsBootstrap(res.needs_bootstrap);
      })
      .finally(() => setLoading(false));
  }

  useEffect(refreshAuth, []);

  async function logout() {
    await api.logout();
    setCoach(null);
    refreshAuth();
  }

  if (loading) return null;
  return <AuthedApp coach={coach} needsBootstrap={needsBootstrap} logout={logout} refreshAuth={refreshAuth} />;
}

function AuthedApp({
  coach,
  needsBootstrap,
  logout,
  refreshAuth,
}: {
  coach: Coach | null;
  needsBootstrap: boolean;
  logout: () => void;
  refreshAuth: () => void;
}) {
  // useLocation (not window.location) so this re-evaluates on every
  // client-side navigation, not just hard page loads -- otherwise clicking
  // "Coach view" while logged out would render the coach UI instead of
  // redirecting to Login, since React Router doesn't re-render plain parent
  // components on navigation, only hook consumers like this one.
  const location = useLocation();
  const isCoachRoute = location.pathname.startsWith("/coach");
  if (!coach && (isCoachRoute || needsBootstrap)) {
    return <Login needsBootstrap={needsBootstrap} />;
  }

  return (
    <>
      <nav className="top-nav">
        <span className="brand">
          <span className="brand-mark">🧪</span> OlympiadPrep
        </span>
        <NavLink to="/" end>
          Home
        </NavLink>
        <span style={{ marginLeft: "auto" }} className="nav-user">
          {coach ? (
            <>
              <span className="avatar">{(coach.name || "?").slice(0, 1).toUpperCase()}</span>
              <span className="muted">{coach.name || "Pending sign-in"}</span>
              <button onClick={logout}>Logout</button>
            </>
          ) : (
            <span className="muted">Student mode</span>
          )}
        </span>
      </nav>
      <div className="app-shell">
        <Routes>
          <Route path="/" element={<Home coach={coach} onCoachAdded={refreshAuth} />} />
          <Route path="/coach/:topicId" element={<CoachTopicBuilder />} />
          <Route path="/coach/:topicId/assessment" element={<CoachAssessment />} />
          <Route path="/student/:topicId" element={<StudentPractice />} />
          <Route path="/student/:topicId/test/:assessmentId" element={<StudentTest />} />
        </Routes>
      </div>
    </>
  );
}
