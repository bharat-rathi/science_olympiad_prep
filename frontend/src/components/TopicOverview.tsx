import { useState } from "react";
import { Topic } from "../api/client";

const SECTIONS: { key: keyof Topic; label: string }[] = [
  { key: "overview_what", label: "What is this event?" },
  { key: "overview_learn", label: "What will kids learn?" },
  { key: "overview_assessed", label: "How is it assessed?" },
  { key: "overview_theme_2027", label: "2027 theme" },
  { key: "overview_notes", label: "Good to know" },
];

// Reference overview for the official pre-seeded events -- empty for a
// coach-created custom topic or sub-topic, in which case this renders
// nothing at all rather than an empty card.
export default function TopicOverview({ topic }: { topic: Topic }) {
  const [open, setOpen] = useState(true);
  const sections = SECTIONS.filter((s) => (topic[s.key] as string)?.trim());
  if (sections.length === 0) return null;

  return (
    <div className="card stack" style={{ marginBottom: 20 }}>
      <div className="row" style={{ justifyContent: "space-between" }}>
        <strong>Event overview</strong>
        <button onClick={() => setOpen((v) => !v)}>{open ? "Collapse" : "Expand"}</button>
      </div>
      {open && (
        <div className="stack">
          {sections.map((s) => (
            <div key={s.key}>
              <div className="muted" style={{ fontWeight: 600, marginBottom: 2 }}>
                {s.label}
              </div>
              <p style={{ margin: 0, whiteSpace: "pre-wrap" }}>{topic[s.key] as string}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
