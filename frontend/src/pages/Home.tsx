import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, Coach, Topic } from "../api/client";

export default function Home({ coach, onCoachAdded }: { coach: Coach | null; onCoachAdded: () => void }) {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [showNew, setShowNew] = useState(false);
  const [eventName, setEventName] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const [showAddCoach, setShowAddCoach] = useState(false);
  const [coachName, setCoachName] = useState("");
  const [coachPassword, setCoachPassword] = useState("");
  const [coachError, setCoachError] = useState("");
  const [coachMessage, setCoachMessage] = useState("");

  useEffect(() => {
    api.listTopics().then(setTopics);
  }, []);

  async function createTopic() {
    if (!name.trim()) return;
    const topic = await api.createTopic({ event_name: eventName || name, name, description });
    setTopics((prev) => [...prev, topic]);
    setShowNew(false);
    setEventName("");
    setName("");
    setDescription("");
  }

  async function addCoach() {
    setCoachError("");
    setCoachMessage("");
    try {
      const created = await api.register(coachName.trim(), coachPassword);
      setCoachMessage(`Added ${created.name} -- share their password with them directly.`);
      setCoachName("");
      setCoachPassword("");
      onCoachAdded();
    } catch (err) {
      setCoachError(err instanceof Error ? err.message : String(err));
    }
  }

  return (
    <div>
      <h1>Topics</h1>
      <p className="muted">
        Pick a topic to coach or practice. A topic's video coverage is used only where it's
        actually useful -- see each concept's source tag once you're inside a topic.
      </p>

      <div className="stack">
        {topics.map((t) => (
          <div className="card" key={t.id}>
            <div className="row" style={{ justifyContent: "space-between" }}>
              <div>
                <strong>{t.name}</strong>
                <div className="muted">
                  {t.event_name}
                  {t.created_by ? ` · added by ${t.created_by}` : ""}
                </div>
              </div>
              <div className="row">
                <Link to={`/coach/${t.id}`}>
                  <button>Coach view</button>
                </Link>
                <Link to={`/student/${t.id}`}>
                  <button className="primary">Student view</button>
                </Link>
              </div>
            </div>
          </div>
        ))}
      </div>

      {coach ? (
        showNew ? (
          <div className="card stack">
            <input placeholder="Topic name (e.g. Optics - refraction)" value={name} onChange={(e) => setName(e.target.value)} />
            <input placeholder="Event name (e.g. Roller Coaster)" value={eventName} onChange={(e) => setEventName(e.target.value)} />
            <textarea placeholder="Short description" value={description} onChange={(e) => setDescription(e.target.value)} />
            <div className="row">
              <button className="primary" onClick={createTopic}>
                Create topic
              </button>
              <button onClick={() => setShowNew(false)}>Cancel</button>
            </div>
          </div>
        ) : (
          <button onClick={() => setShowNew(true)}>+ New topic</button>
        )
      ) : (
        <p className="muted">Log in as a coach to add a topic.</p>
      )}

      {coach && (
        <>
          <h2>Coaches</h2>
          {showAddCoach ? (
            <div className="card stack">
              <input placeholder="Teammate's name" value={coachName} onChange={(e) => setCoachName(e.target.value)} />
              <input
                type="password"
                placeholder="Set a password for them (8+ characters)"
                value={coachPassword}
                onChange={(e) => setCoachPassword(e.target.value)}
              />
              {coachError && <p style={{ color: "var(--danger)" }}>{coachError}</p>}
              {coachMessage && <p className="muted">{coachMessage}</p>}
              <div className="row">
                <button className="primary" onClick={addCoach}>
                  Add coach
                </button>
                <button onClick={() => setShowAddCoach(false)}>Done</button>
              </div>
            </div>
          ) : (
            <button onClick={() => setShowAddCoach(true)}>+ Add a coach</button>
          )}
        </>
      )}
    </div>
  );
}
