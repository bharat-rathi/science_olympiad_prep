import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api, ConceptTerm, Resource, Topic } from "../api/client";

export default function CoachTopicBuilder() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [resources, setResources] = useState<Resource[]>([]);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const [resTitle, setResTitle] = useState("");
  const [resText, setResText] = useState("");
  const [resUrl, setResUrl] = useState("");

  const [linkUrl, setLinkUrl] = useState("");
  const [linkBusy, setLinkBusy] = useState(false);
  const [linkError, setLinkError] = useState("");

  function refresh() {
    api.getTopic(id).then(setTopic);
    api.listResources(id).then(setResources);
    api.listConcepts(id).then(setConcepts);
  }

  useEffect(refresh, [id]);

  async function addTextResource() {
    if (!resText.trim()) return;
    await api.addTextResource(id, { title: resTitle || "Untitled resource", text: resText, source_url: resUrl });
    setResTitle("");
    setResText("");
    setResUrl("");
    refresh();
  }

  async function addLink() {
    if (!linkUrl.trim()) return;
    setLinkBusy(true);
    setLinkError("");
    try {
      await api.addLinkResource(id, linkUrl.trim());
      setLinkUrl("");
      refresh();
    } catch (err) {
      setLinkError(err instanceof Error ? err.message : String(err));
    } finally {
      setLinkBusy(false);
    }
  }

  async function uploadFile(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    if (!file) return;
    setBusy(true);
    setError("");
    try {
      await api.uploadMediaResource(id, file);
      refresh();
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
      e.target.value = "";
    }
  }

  async function generate() {
    setBusy(true);
    setError("");
    try {
      await api.generateExplanations(id);
      refresh();
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
    }
  }

  async function toggleApprove(c: ConceptTerm) {
    const updated = await api.updateConcept(id, c.id, { approved: !c.approved });
    setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
  }

  async function editExplanation(c: ConceptTerm, explanation_md: string) {
    const updated = await api.updateConcept(id, c.id, { explanation_md });
    setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
  }

  if (!topic) return <p>Loading...</p>;

  const approvedCount = concepts.filter((c) => c.approved).length;

  return (
    <div>
      <h1>{topic.name}</h1>
      <p className="muted">{topic.description}</p>

      <h2>1. Resources</h2>
      <p className="muted">
        Paste text/link content, or upload a short video/audio clip (or a zip of several). Video is
        one possible source among several -- it's only used where the relevance check below finds
        it actually explains a concept.
      </p>
      <div className="card stack">
        <input placeholder="Resource title" value={resTitle} onChange={(e) => setResTitle(e.target.value)} />
        <input placeholder="Source URL (optional)" value={resUrl} onChange={(e) => setResUrl(e.target.value)} />
        <textarea placeholder="Paste text content" value={resText} onChange={(e) => setResText(e.target.value)} />
        <div className="row">
          <button className="primary" onClick={addTextResource}>
            Add text resource
          </button>
          <label>
            <input type="file" accept=".mp4,.mov,.mkv,.avi,.webm,.mp3,.wav,.m4a,.flac,.zip" onChange={uploadFile} disabled={busy} />
          </label>
        </div>
      </div>

      <div className="card stack">
        <label className="muted">Or paste a link -- the system fetches and reads it directly</label>
        <div className="row">
          <input
            placeholder="https://..."
            value={linkUrl}
            onChange={(e) => setLinkUrl(e.target.value)}
            style={{ flex: 1 }}
          />
          <button className="primary" onClick={addLink} disabled={linkBusy}>
            {linkBusy ? "Fetching..." : "Fetch & add"}
          </button>
        </div>
        {linkError && <p style={{ color: "var(--danger)" }}>{linkError}</p>}
      </div>

      {resources.length > 0 && (
        <div className="stack">
          {resources.map((r) => (
            <div className="card" key={r.id}>
              <span className={`tag ${r.type === "video" ? "video" : ""}`}>{r.type}</span>
              {r.title}
            </div>
          ))}
        </div>
      )}

      <h2>2. Concept explanations</h2>
      <div className="row">
        <button className="primary" onClick={generate} disabled={busy}>
          {busy ? "Working..." : "Generate concept explanations"}
        </button>
        <span className="muted">{approvedCount} approved</span>
      </div>
      {error && <p style={{ color: "var(--danger)" }}>{error}</p>}

      <div className="stack" style={{ marginTop: 12 }}>
        {concepts.map((c) => (
          <div className="card" key={c.id}>
            <div className="row" style={{ justifyContent: "space-between" }}>
              <strong>{c.term}</strong>
              <span className={`tag ${c.video_relevant ? "video" : "general"}`}>
                {c.video_relevant ? "video coverage" : c.source_resource_ids.length ? "team resource" : "general knowledge"}
              </span>
            </div>
            <textarea
              defaultValue={c.explanation_md}
              onBlur={(e) => e.target.value !== c.explanation_md && editExplanation(c, e.target.value)}
            />
            <div className="row">
              <label className="row">
                <input type="checkbox" checked={c.approved} onChange={() => toggleApprove(c)} />
                Approved for assessment
              </label>
            </div>
          </div>
        ))}
      </div>

      <h2>3. Assessment</h2>
      <Link to={`/coach/${id}/assessment`}>
        <button disabled={approvedCount === 0}>Go to assessment editor</button>
      </Link>
      {approvedCount === 0 && <p className="muted">Approve at least one concept first.</p>}
    </div>
  );
}
