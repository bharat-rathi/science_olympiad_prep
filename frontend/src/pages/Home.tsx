import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, Topic } from "../api/client";

export default function Home() {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [showNew, setShowNew] = useState(false);
  const [eventName, setEventName] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

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
                <div className="muted">{t.event_name}</div>
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

      {showNew ? (
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
      )}
    </div>
  );
}
