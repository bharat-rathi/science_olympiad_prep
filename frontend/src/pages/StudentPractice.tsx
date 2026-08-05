import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, Assessment, ConceptTerm, Topic } from "../api/client";

export default function StudentPractice() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [assessment, setAssessment] = useState<Assessment | null>(null);

  useEffect(() => {
    api.getTopic(id).then(setTopic);
    api.listConcepts(id).then((all) => setConcepts(all.filter((c) => c.approved)));
    api.getLatestAssessment(id).then((a) => setAssessment(a && a.status === "published" ? a : null));
  }, [id]);

  if (!topic) return <p>Loading...</p>;

  return (
    <div>
      <div className="page-header">
        <h1>{topic.name}</h1>
        <p className="muted">{topic.description}</p>
      </div>

      {assessment && (
        <div className="card row" style={{ justifyContent: "space-between" }}>
          <span>A practice test is ready for this topic.</span>
          <Link to={`/student/${id}/test/${assessment.id}`}>
            <button className="primary">Start test</button>
          </Link>
        </div>
      )}

      <h2>Concepts to know</h2>
      <div className="stack">
        {concepts.map((c) => (
          <div className="card" key={c.id}>
            <div className="row" style={{ justifyContent: "space-between" }}>
              <strong>{c.term}</strong>
              <span className={`tag ${c.video_relevant ? "video" : "general"}`}>
                {c.video_relevant ? "from team video" : c.source_resource_ids.length ? "from team resource" : "general knowledge"}
              </span>
            </div>
            <p>{c.explanation_md}</p>
          </div>
        ))}
        {concepts.length === 0 && <p className="muted">Your coach hasn't approved any concepts for this topic yet.</p>}
      </div>
    </div>
  );
}
