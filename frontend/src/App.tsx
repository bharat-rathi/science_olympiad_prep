import { NavLink, Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import CoachTopicBuilder from "./pages/CoachTopicBuilder";
import CoachAssessment from "./pages/CoachAssessment";
import StudentPractice from "./pages/StudentPractice";
import StudentTest from "./pages/StudentTest";

export default function App() {
  return (
    <>
      <nav className="top-nav">
        <span className="brand">🧪 Science Olympiad Coach</span>
        <NavLink to="/" end>
          Home
        </NavLink>
      </nav>
      <div className="app-shell">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/coach/:topicId" element={<CoachTopicBuilder />} />
          <Route path="/coach/:topicId/assessment" element={<CoachAssessment />} />
          <Route path="/student/:topicId" element={<StudentPractice />} />
          <Route path="/student/:topicId/test/:assessmentId" element={<StudentTest />} />
        </Routes>
      </div>
    </>
  );
}
