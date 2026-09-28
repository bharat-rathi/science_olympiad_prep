import { useEffect, useState } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { api, ScheduleEntry, SuggestedSession, Topic } from "../api/client";

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

  const [numSessions, setNumSessions] = useState(4);
  const [suggested, setSuggested] = useState<(SuggestedSession & { date: string })[] | null>(null);
  const [suggestBusy, setSuggestBusy] = useState(false);
  const [suggestError, setSuggestError] = useState("");
  const [acceptBusy, setAcceptBusy] = useState(false);

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

  async function suggestSequence() {
    setSuggestBusy(true);
    setSuggestError("");
    try {
      const sessions = await api.suggestSequence(id, numSessions);
      setSuggested(sessions.map((s) => ({ ...s, date: "" })));
    } catch (err) {
      setSuggestError(err instanceof Error ? err.message : String(err));
    } finally {
      setSuggestBusy(false);
    }
  }

  function updateSuggested(index: number, field: "title" | "description" | "date", value: string) {
    setSuggested((prev) => (prev ? prev.map((s, i) => (i === index ? { ...s, [field]: value } : s)) : prev));
  }

  function removeSuggested(index: number) {
    setSuggested((prev) => (prev ? prev.filter((_, i) => i !== index) : prev));
  }

  async function acceptSequence() {
    if (!suggested || !topic) return;
    setAcceptBusy(true);
    setSuggestError("");
    try {
      for (const session of suggested) {
        if (!session.title.trim()) continue;
        const subTopic = await api.createTopic({
          event_name: topic.event_name,
          name: session.title.trim(),
          description: session.description,
          assessment_type: topic.assessment_type,
          parent_topic_id: topic.id,
        });
        if (session.date) {
          await api.createScheduleEntry(subTopic.id, {
            scheduled_at: new Date(session.date).toISOString(),
            title: session.title.trim(),
          });
        }
      }
      setSuggested(null);
      refresh();
    } catch (err) {
      setSuggestError(err instanceof Error ? err.message : String(err));
    } finally {
      setAcceptBusy(false);
    }
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

      <h2>Suggest a teaching sequence</h2>
      <p className="muted">
        Let AI propose how to break {topic.name} into a set of session-sized sub-topics, in teaching
        order -- review and edit before creating any of them.
      </p>
      <div className="card stack">
        <label className="row">
          Number of sessions
          <input
            type="number"
            min={1}
            max={12}
            value={numSessions}
            onChange={(e) => setNumSessions(Number(e.target.value) || 1)}
            style={{ width: 60 }}
          />
        </label>
        {suggestError && <p style={{ color: "var(--danger)" }}>{suggestError}</p>}
        <button className="accent" onClick={suggestSequence} disabled={suggestBusy}>
          {suggestBusy ? "Thinking..." : "✨ Suggest sequence"}
        </button>
      </div>

      {suggested && (
        <div className="stack" style={{ marginTop: 12 }}>
          {suggested.map((s, i) => (
            <div className="card stack" key={i}>
              <div className="row" style={{ justifyContent: "space-between" }}>
                <input
                  value={s.title}
                  onChange={(e) => updateSuggested(i, "title", e.target.value)}
                  style={{ flex: 1, fontWeight: 600 }}
                />
                <button onClick={() => removeSuggested(i)}>Remove</button>
              </div>
              <textarea value={s.description} onChange={(e) => updateSuggested(i, "description", e.target.value)} />
              <label className="muted">
                Schedule for (optional)
                <input
                  type="datetime-local"
                  value={s.date}
                  onChange={(e) => updateSuggested(i, "date", e.target.value)}
                  style={{ display: "block", marginTop: 4 }}
                />
              </label>
            </div>
          ))}
          <div className="row">
            <button className="primary" onClick={acceptSequence} disabled={acceptBusy || suggested.length === 0}>
              {acceptBusy ? "Creating..." : `Create ${suggested.length} sub-topic${suggested.length === 1 ? "" : "s"}`}
            </button>
            <button onClick={() => setSuggested(null)}>Discard</button>
          </div>
        </div>
      )}

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
