import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api, Coach, Topic } from "../api/client";

export default function Home({ coach, onCoachAdded }: { coach: Coach | null; onCoachAdded: () => void }) {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [showNew, setShowNew] = useState(false);
  const [eventName, setEventName] = useState("");
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const [showInvite, setShowInvite] = useState(false);
  const [inviteEmail, setInviteEmail] = useState("");
  const [inviteError, setInviteError] = useState("");
  const [inviteMessage, setInviteMessage] = useState("");

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

  async function invite() {
    setInviteError("");
    setInviteMessage("");
    try {
      await api.inviteCoach(inviteEmail.trim().toLowerCase());
      setInviteMessage(`Invited ${inviteEmail.trim()} -- they can now sign in with that Google account.`);
      setInviteEmail("");
      onCoachAdded();
    } catch (err) {
      setInviteError(err instanceof Error ? err.message : String(err));
    }
  }

  const publishedCount = topics.filter((t) => t.content_published).length;

  return (
    <div>
      <div className="hero">
        <h1>Empower Your Future Scientists</h1>
        <p>
          Pick a topic to coach or practice. A topic's video coverage is used only where it's
          actually useful -- see each concept's source tag once you're inside a topic.
        </p>
      </div>

      {coach && topics.length > 0 && (
        <div className="stat-row">
          <div className="stat-tile">
            <span className="stat-label">Topics</span>
            <span className="stat-value">{topics.length}</span>
          </div>
          <div className="stat-tile alt">
            <span className="stat-label">Live for students</span>
            <span className="stat-value">{publishedCount}</span>
          </div>
        </div>
      )}

      <h2>Topics</h2>
      <div className="grid-2">
        {topics.map((t) => (
          <div className="card hoverable accent-top stack" key={t.id}>
            <div className="row" style={{ justifyContent: "space-between", alignItems: "flex-start" }}>
              <div>
                <span className="card-title">{t.name}</span>
                <div className="muted">
                  {t.event_name}
                  {t.created_by ? ` · added by ${t.created_by}` : ""}
                </div>
              </div>
              <span className={`tag ${t.content_published ? "success" : "general"}`}>
                {t.content_published ? "Live" : "Draft"}
              </span>
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
        ))}
        {topics.length === 0 && <p className="muted">No topics yet.</p>}
      </div>

      {coach ? (
        showNew ? (
          <div className="card stack">
            <input placeholder="Topic name (e.g. Optics - refraction)" value={name} onChange={(e) => setName(e.target.value)} />
            <input placeholder="Event name (e.g. Roller Coaster)" value={eventName} onChange={(e) => setEventName(e.target.value)} />
            <textarea placeholder="Short description" value={description} onChange={(e) => setDescription(e.target.value)} />
            <div className="row">
              <button className="accent" onClick={createTopic}>
                Create topic
              </button>
              <button onClick={() => setShowNew(false)}>Cancel</button>
            </div>
          </div>
        ) : (
          <button className="accent" onClick={() => setShowNew(true)}>
            + New topic
          </button>
        )
      ) : (
        <p className="muted">Log in as a coach to add a topic.</p>
      )}

      {coach && (
        <>
          <h2>Coaches</h2>
          {showInvite ? (
            <div className="card stack">
              <input
                type="email"
                placeholder="Teammate's Google account email"
                value={inviteEmail}
                onChange={(e) => setInviteEmail(e.target.value)}
              />
              {inviteError && <p style={{ color: "var(--danger)" }}>{inviteError}</p>}
              {inviteMessage && <p className="muted">{inviteMessage}</p>}
              <div className="row">
                <button className="primary" onClick={invite}>
                  Send invite
                </button>
                <button onClick={() => setShowInvite(false)}>Done</button>
              </div>
            </div>
          ) : (
            <button onClick={() => setShowInvite(true)}>+ Invite a coach</button>
          )}
        </>
      )}
    </div>
  );
}
