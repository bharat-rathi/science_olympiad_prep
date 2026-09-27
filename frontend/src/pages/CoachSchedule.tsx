import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { api, ScheduleEntry, Topic } from "../api/client";

function toLocalInputValue(iso: string): string {
  // <input type="datetime-local"> wants "YYYY-MM-DDTHH:mm" in local time,
  // not the ISO string's UTC representation.
  const d = new Date(iso);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}T${pad(d.getHours())}:${pad(d.getMinutes())}`;
}

export default function CoachSchedule() {
  const { topicId } = useParams();
  const id = Number(topicId);
  const navigate = useNavigate();

  const [topic, setTopic] = useState<Topic | null>(null);
  const [entries, setEntries] = useState<ScheduleEntry[]>([]);
  const [subTopics, setSubTopics] = useState<Topic[]>([]);

  const [scheduledAt, setScheduledAt] = useState("");
  const [title, setTitle] = useState("");
  const [notes, setNotes] = useState("");
  const [asSubTopic, setAsSubTopic] = useState(false);
  const [subTopicName, setSubTopicName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  function refresh() {
    api.getTopic(id).then(setTopic);
    api.listSchedule(id).then(setEntries);
    api.listSubTopics(id).then(setSubTopics);
  }

  useEffect(refresh, [id]);

  async function addEntry() {
    if (!scheduledAt || (asSubTopic && !subTopicName.trim())) return;
    setBusy(true);
    setError("");
    try {
      const scheduled_at = new Date(scheduledAt).toISOString();
      if (asSubTopic && topic) {
        const subTopic = await api.createTopic({
          event_name: topic.event_name,
          name: subTopicName.trim(),
          assessment_type: topic.assessment_type,
          parent_topic_id: topic.id,
        });
        await api.createScheduleEntry(subTopic.id, { scheduled_at, title, notes });
        // Straight into the new sub-topic's own builder -- that's the "deep
        // dive" this schedule entry exists to set up.
        navigate(`/coach/${subTopic.id}`);
        return;
      }
      await api.createScheduleEntry(id, { scheduled_at, title, notes });
      setScheduledAt("");
      setTitle("");
      setNotes("");
      setAsSubTopic(false);
      setSubTopicName("");
      refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setBusy(false);
    }
  }

  async function removeEntry(entryId: number) {
    await api.deleteScheduleEntry(id, entryId);
    setEntries((prev) => prev.filter((e) => e.id !== entryId));
  }

  if (!topic) return <p>Loading...</p>;

  return (
    <div>
      <div className="page-header">
        <Link to={`/coach/${id}`} className="muted">
          ← {topic.name}
        </Link>
        <h1>Schedule</h1>
        <p className="muted">Plan when to study this topic, or spin off a focused sub-topic for a deep dive.</p>
      </div>

      <div className="stack">
        {entries
          .slice()
          .sort((a, b) => a.scheduled_at.localeCompare(b.scheduled_at))
          .map((e) => (
            <div className="card row" style={{ justifyContent: "space-between" }} key={e.id}>
              <span>
                <strong>{new Date(e.scheduled_at).toLocaleString()}</strong>
                {e.title && <> — {e.title}</>}
                {e.notes && <div className="muted">{e.notes}</div>}
              </span>
              <button onClick={() => removeEntry(e.id)}>Remove</button>
            </div>
          ))}
        {entries.length === 0 && <p className="muted">No sessions scheduled for this topic yet.</p>}
      </div>

      <h2>+ Schedule a session</h2>
      <div className="card stack">
        <label className="muted">
          Date & time
          <input
            type="datetime-local"
            value={scheduledAt}
            onChange={(e) => setScheduledAt(e.target.value)}
            style={{ display: "block", marginTop: 4 }}
          />
        </label>
        <input placeholder="Title (optional)" value={title} onChange={(e) => setTitle(e.target.value)} />
        <textarea placeholder="Notes (optional)" value={notes} onChange={(e) => setNotes(e.target.value)} />
        <label className="row">
          <input type="checkbox" checked={asSubTopic} onChange={(e) => setAsSubTopic(e.target.checked)} />
          Create a new sub-topic for this session (a focused deep dive under {topic.name})
        </label>
        {asSubTopic && (
          <input
            placeholder={`Sub-topic name (e.g. "${topic.name}: track friction")`}
            value={subTopicName}
            onChange={(e) => setSubTopicName(e.target.value)}
          />
        )}
        {error && <p style={{ color: "var(--danger)" }}>{error}</p>}
        <button className="primary" onClick={addEntry} disabled={busy}>
          {busy ? "Saving..." : asSubTopic ? "Create sub-topic & schedule" : "Schedule session"}
        </button>
      </div>

      {subTopics.length > 0 && (
        <>
          <h2>Sub-topics</h2>
          <div className="stack">
            {subTopics.map((t) => (
              <Link to={`/coach/${t.id}`} key={t.id}>
                <div className="card hoverable">{t.name}</div>
              </Link>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
