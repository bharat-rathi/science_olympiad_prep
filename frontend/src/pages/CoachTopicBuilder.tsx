import { useRef, useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import { api, ConceptTerm, Diagram, Resource, Topic } from "../api/client";
import TopicChat from "../components/TopicChat";

const RESOURCE_ICON: Record<string, string> = {
  pdf: "📄",
  video: "🎬",
  text: "📝",
  link: "🔗",
  research: "🔍",
};

export default function CoachTopicBuilder() {
  const { topicId } = useParams();
  const id = Number(topicId);

  const [topic, setTopic] = useState<Topic | null>(null);
  const [resources, setResources] = useState<Resource[]>([]);
  const [concepts, setConcepts] = useState<ConceptTerm[]>([]);
  const [diagrams, setDiagrams] = useState<Diagram[]>([]);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  const fileInputRef = useRef<HTMLInputElement>(null);
  const [dragActive, setDragActive] = useState(false);

  const [showPasteText, setShowPasteText] = useState(false);
  const [resTitle, setResTitle] = useState("");
  const [resText, setResText] = useState("");
  const [resUrl, setResUrl] = useState("");

  const [linkUrl, setLinkUrl] = useState("");
  const [linkBusy, setLinkBusy] = useState(false);
  const [linkError, setLinkError] = useState("");

  const [expandedResourceIds, setExpandedResourceIds] = useState<Set<number>>(new Set());
  const [deletingResourceId, setDeletingResourceId] = useState<number | null>(null);
  const [expandedConceptIds, setExpandedConceptIds] = useState<Set<number>>(new Set());

  const [feedbackDrafts, setFeedbackDrafts] = useState<Record<number, string>>({});
  const [refiningId, setRefiningId] = useState<number | null>(null);
  const [imagingId, setImagingId] = useState<number | null>(null);
  const [storyBusy, setStoryBusy] = useState(false);
  const [publishBusy, setPublishBusy] = useState(false);
  const [approveAllBusy, setApproveAllBusy] = useState(false);

  function refresh() {
    api.getTopic(id).then(setTopic);
    api.listResources(id).then(setResources);
    api.listConcepts(id).then(setConcepts);
    api.listDiagrams(id).then(setDiagrams);
  }

  useEffect(refresh, [id]);

  // Video resources (Drive links, uploaded video/audio) process in the
  // background and start out status="pending" -- poll while any are still
  // pending so the UI picks up "ready"/"failed" without a manual refresh.
  useEffect(() => {
    if (!resources.some((r) => r.status === "pending")) return;
    const interval = setInterval(() => {
      api.listResources(id).then(setResources);
    }, 5000);
    return () => clearInterval(interval);
  }, [id, resources]);

  async function addTextResource() {
    if (!resText.trim()) return;
    await api.addTextResource(id, { title: resTitle || "Untitled resource", text: resText, source_url: resUrl });
    setResTitle("");
    setResText("");
    setResUrl("");
    setShowPasteText(false);
    refresh();
  }

  function toggleResourceExpand(resourceId: number) {
    setExpandedResourceIds((prev) => {
      const next = new Set(prev);
      if (next.has(resourceId)) next.delete(resourceId);
      else next.add(resourceId);
      return next;
    });
  }

  async function removeResource(r: Resource) {
    if (!window.confirm(`Remove "${r.title}"? Its source content will no longer count toward concept generation.`)) return;
    setDeletingResourceId(r.id);
    try {
      await api.deleteResource(id, r.id);
      setResources((prev) => prev.filter((x) => x.id !== r.id));
      setDiagrams((prev) => prev.filter((d) => d.resource_id !== r.id));
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setDeletingResourceId(null);
    }
  }

  function toggleConceptExpand(conceptId: number) {
    setExpandedConceptIds((prev) => {
      const next = new Set(prev);
      if (next.has(conceptId)) next.delete(conceptId);
      else next.add(conceptId);
      return next;
    });
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

  async function doUpload(file: File) {
    setBusy(true);
    setError("");
    try {
      await api.uploadMediaResource(id, file);
      refresh();
    } catch (err) {
      setError(String(err));
    } finally {
      setBusy(false);
    }
  }

  function onFileInputChange(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0];
    e.target.value = "";
    if (file) doUpload(file);
  }

  function onDrop(e: React.DragEvent<HTMLDivElement>) {
    e.preventDefault();
    setDragActive(false);
    const file = e.dataTransfer.files?.[0];
    if (file) doUpload(file);
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

  async function approveAll() {
    const toApprove = concepts.filter((c) => !c.approved);
    if (toApprove.length === 0) return;
    setApproveAllBusy(true);
    try {
      const updates = await Promise.all(toApprove.map((c) => api.updateConcept(id, c.id, { approved: true })));
      const byId = new Map(updates.map((u) => [u.id, u]));
      setConcepts((prev) => prev.map((x) => byId.get(x.id) || x));
    } finally {
      setApproveAllBusy(false);
    }
  }

  async function editExplanation(c: ConceptTerm, explanation_md: string) {
    const updated = await api.updateConcept(id, c.id, { explanation_md });
    setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
  }

  async function editAnalogy(c: ConceptTerm, analogy: string) {
    const updated = await api.updateConcept(id, c.id, { analogy });
    setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
  }

  async function editWhyItMatters(c: ConceptTerm, why_it_matters: string) {
    const updated = await api.updateConcept(id, c.id, { why_it_matters });
    setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
  }

  async function refineConcept(c: ConceptTerm) {
    const feedback = (feedbackDrafts[c.id] || "").trim();
    if (!feedback) return;
    setRefiningId(c.id);
    try {
      const updated = await api.refineConcept(id, c.id, feedback);
      setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
      setFeedbackDrafts((prev) => ({ ...prev, [c.id]: "" }));
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setRefiningId(null);
    }
  }

  async function generateImage(c: ConceptTerm) {
    setImagingId(c.id);
    try {
      const updated = await api.generateConceptImage(id, c.id);
      setConcepts((prev) => prev.map((x) => (x.id === c.id ? updated : x)));
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setImagingId(null);
    }
  }

  async function generateStory() {
    setStoryBusy(true);
    setError("");
    try {
      const updated = await api.generateStory(id);
      setTopic(updated);
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setStoryBusy(false);
    }
  }

  async function editStory(story_md: string) {
    const updated = await api.updateStory(id, story_md);
    setTopic(updated);
  }

  async function togglePublish() {
    if (!topic) return;
    setPublishBusy(true);
    try {
      const updated = topic.content_published ? await api.unpublishContent(id) : await api.publishContent(id);
      setTopic(updated);
    } finally {
      setPublishBusy(false);
    }
  }

  if (!topic) return <p>Loading...</p>;

  const approvedCount = concepts.filter((c) => c.approved).length;

  return (
    <div>
      <div className="page-header">
        <h1>{topic.name}</h1>
        <p className="muted">{topic.description}</p>
      </div>

      <h2>
        <span className="step-badge">1</span> Resources
      </h2>
      <p className="muted">
        Upload a document, PDF, video/audio clip (or a zip of several), paste a link, or type a
        topic to research. Video is one possible source among several -- it's only used where the
        relevance check below finds it actually explains a concept.
      </p>

      <div className="card">
        <div
          className={`dropzone ${dragActive ? "active" : ""}`}
          onDragOver={(e) => {
            e.preventDefault();
            setDragActive(true);
          }}
          onDragLeave={() => setDragActive(false)}
          onDrop={onDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          <input
            ref={fileInputRef}
            type="file"
            accept=".mp4,.mov,.mkv,.avi,.webm,.mp3,.wav,.m4a,.flac,.pdf,.zip"
            onChange={onFileInputChange}
            disabled={busy}
            style={{ display: "none" }}
          />
          <div className="dropzone-icon">📤</div>
          <strong>{busy ? "Uploading..." : "Drag and drop a file here, or click to browse"}</strong>
          <div className="row" style={{ justifyContent: "center", marginTop: 10 }}>
            <span className="tag">PDF</span>
            <span className="tag">Video / Audio</span>
            <span className="tag">Zip of several</span>
          </div>
        </div>

        <div className="dropzone-divider">or</div>

        <div className="row">
          <input
            placeholder="Paste a link (YouTube, Google Drive video, or any web page), or type a topic to research"
            value={linkUrl}
            onChange={(e) => setLinkUrl(e.target.value)}
            style={{ flex: 1 }}
          />
          <button className="primary" onClick={addLink} disabled={linkBusy}>
            {linkBusy ? "Working..." : "Add"}
          </button>
        </div>
        {linkError && <p style={{ color: "var(--danger)" }}>{linkError}</p>}

        {showPasteText ? (
          <div className="stack" style={{ marginTop: 14, paddingTop: 14, borderTop: "1px solid var(--border)" }}>
            <input placeholder="Resource title" value={resTitle} onChange={(e) => setResTitle(e.target.value)} />
            <input placeholder="Source URL (optional)" value={resUrl} onChange={(e) => setResUrl(e.target.value)} />
            <textarea placeholder="Paste text content" value={resText} onChange={(e) => setResText(e.target.value)} />
            <div className="row">
              <button className="primary" onClick={addTextResource}>
                Add text resource
              </button>
              <button onClick={() => setShowPasteText(false)}>Cancel</button>
            </div>
          </div>
        ) : (
          <button className="dropzone-text-toggle" onClick={() => setShowPasteText(true)}>
            + Paste text directly instead
          </button>
        )}
      </div>

      {error && <p style={{ color: "var(--danger)" }}>{error}</p>}

      {resources.length > 0 && (
        <div className="stack">
          <div className="muted" style={{ fontWeight: 600, fontSize: "0.8rem", textTransform: "uppercase", letterSpacing: "0.04em" }}>
            Uploaded resources ({resources.length}) -- always here to review or clean up
          </div>
          {resources.map((r) => {
            const content = r.type === "video" ? r.transcript : r.raw_text;
            const isExpanded = expandedResourceIds.has(r.id);
            const isDeleting = deletingResourceId === r.id;
            return (
              <div className="card" key={r.id}>
                <div className="row" style={{ justifyContent: "space-between" }}>
                  <span className="row" style={{ gap: 8 }}>
                    <span style={{ fontSize: "1.1rem" }}>{RESOURCE_ICON[r.type] || "📎"}</span>
                    <span className={`tag ${r.type === "video" ? "video" : r.type === "research" ? "general" : ""}`}>
                      {r.type}
                    </span>
                    {r.status === "pending" && <span className="tag general">Processing...</span>}
                    {r.status === "failed" && <span className="tag" style={{ background: "var(--danger-soft)", color: "var(--danger)" }}>Failed</span>}
                    <span className="card-title" style={{ fontSize: "1rem" }}>{r.title}</span>
                  </span>
                  <div className="row">
                    {content && (
                      <button onClick={() => toggleResourceExpand(r.id)}>
                        {isExpanded ? "Hide content" : "View content"}
                      </button>
                    )}
                    <button onClick={() => removeResource(r)} disabled={isDeleting}>
                      {isDeleting ? "Removing..." : "Remove"}
                    </button>
                  </div>
                </div>
                <div className="muted" style={{ fontSize: "0.78rem", marginTop: 4 }}>
                  Added {new Date(r.created_at).toLocaleDateString(undefined, { month: "short", day: "numeric", year: "numeric" })}
                  {r.source_url && (
                    <>
                      {" · "}
                      <a href={r.source_url} target="_blank" rel="noreferrer">
                        source link
                      </a>
                    </>
                  )}
                </div>
                {r.status === "failed" && r.error_message && (
                  <p style={{ color: "var(--danger)", fontSize: "0.85rem", marginTop: 8, marginBottom: 0 }}>
                    {r.error_message}
                  </p>
                )}
                {isExpanded && content && (
                  <p className="muted" style={{ whiteSpace: "pre-wrap", marginTop: 10, marginBottom: 0 }}>
                    {content}
                  </p>
                )}
              </div>
            );
          })}
        </div>
      )}

      {diagrams.length > 0 && (
        <div className="stack">
          <div className="muted" style={{ fontWeight: 600, fontSize: "0.8rem", textTransform: "uppercase", letterSpacing: "0.04em" }}>
            Diagrams extracted from your PDFs ({diagrams.length})
          </div>
          <div className="diagram-grid">
            {diagrams.map((d) => (
              <div className="card diagram-card" key={d.id}>
                <img src={d.image_data_url} alt={d.caption} />
                <p className="muted">{d.caption}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      <h2>
        <span className="step-badge">2</span> Ask about this content
      </h2>
      <p className="muted">Sanity-check retrieval against what you've just uploaded before generating concepts below.</p>
      <TopicChat topicId={id} />

      <h2>
        <span className="step-badge">3</span> Concept explanations
      </h2>
      <div className="row" style={{ justifyContent: "space-between" }}>
        <div className="row">
          <button className="accent" onClick={generate} disabled={busy}>
            {busy ? "Working..." : "✨ Generate concept explanations"}
          </button>
          <span className="muted">
            {approvedCount} of {concepts.length} approved
          </span>
        </div>
        {concepts.length > 0 && approvedCount < concepts.length && (
          <button onClick={approveAll} disabled={approveAllBusy}>
            {approveAllBusy ? "Approving..." : `Approve all (${concepts.length - approvedCount})`}
          </button>
        )}
      </div>

      <div className="stack" style={{ marginTop: 12 }}>
        {concepts.map((c) => {
          const isEditing = expandedConceptIds.has(c.id);
          return (
            <div className="card accent-top concept-card" key={c.id}>
              <div className="row" style={{ justifyContent: "space-between", alignItems: "flex-start" }}>
                <div className="row" style={{ gap: 12 }}>
                  {c.image_data_url && <img src={c.image_data_url} alt={c.term} className="concept-thumb" />}
                  <div>
                    <span className="card-title">{c.term}</span>
                    <div>
                      <span className={`tag ${c.video_relevant ? "video" : "general"}`}>
                        {c.video_relevant ? "video coverage" : c.source_resource_ids.length ? "team resource" : "general knowledge"}
                      </span>
                    </div>
                  </div>
                </div>
                <button className={c.approved ? "primary" : ""} onClick={() => toggleApprove(c)}>
                  {c.approved ? "✓ Approved" : "Approve"}
                </button>
              </div>

              {c.analogy && <p className="flashcard-analogy concept-analogy">{c.analogy}</p>}

              {!isEditing ? (
                <button className="dropzone-text-toggle" onClick={() => toggleConceptExpand(c.id)}>
                  Edit explanation, analogy, why it matters, or image →
                </button>
              ) : (
                <div className="stack" style={{ marginTop: 8 }}>
                  <label className="muted">Explanation</label>
                  <textarea
                    defaultValue={c.explanation_md}
                    onBlur={(e) => e.target.value !== c.explanation_md && editExplanation(c, e.target.value)}
                  />
                  <label className="muted">Analogy</label>
                  <textarea
                    defaultValue={c.analogy}
                    placeholder="A short real-world comparison for the flashcard back"
                    style={{ minHeight: 50 }}
                    onBlur={(e) => e.target.value !== c.analogy && editAnalogy(c, e.target.value)}
                  />
                  <label className="muted">Why it matters</label>
                  <textarea
                    defaultValue={c.why_it_matters}
                    placeholder="How this concept connects to an actual decision or rule in this event"
                    style={{ minHeight: 50 }}
                    onBlur={(e) => e.target.value !== c.why_it_matters && editWhyItMatters(c, e.target.value)}
                  />
                  <div className="row">
                    <input
                      placeholder="Feedback to refine this concept (e.g. 'too technical', 'add an example')"
                      style={{ flex: 1 }}
                      value={feedbackDrafts[c.id] || ""}
                      onChange={(e) => setFeedbackDrafts((prev) => ({ ...prev, [c.id]: e.target.value }))}
                    />
                    <button onClick={() => refineConcept(c)} disabled={refiningId === c.id || !(feedbackDrafts[c.id] || "").trim()}>
                      {refiningId === c.id ? "Refining..." : "Refine"}
                    </button>
                  </div>
                  {c.image_data_url && <img src={c.image_data_url} alt={c.term} className="concept-image-preview" />}
                  <div className="row">
                    <button onClick={() => generateImage(c)} disabled={imagingId === c.id}>
                      {imagingId === c.id ? "Drawing..." : c.image_data_url ? "Regenerate image" : "Generate image"}
                    </button>
                    <button onClick={() => toggleConceptExpand(c.id)} style={{ marginLeft: "auto" }}>
                      Done editing
                    </button>
                  </div>
                </div>
              )}
            </div>
          );
        })}
      </div>

      <h2>
        <span className="step-badge">4</span> Story (optional)
      </h2>
      <p className="muted">
        Weaves the approved concepts into one short narrative students can read as a story instead
        of a list of definitions. Only generated when you ask for it.
      </p>
      <div className="card stack">
        <button className="accent" onClick={generateStory} disabled={storyBusy || approvedCount === 0}>
          {storyBusy ? "Writing..." : topic.story_md ? "✨ Regenerate story" : "✨ Generate story"}
        </button>
        {approvedCount === 0 && <p className="muted">Approve at least one concept first.</p>}
        {topic.story_md && (
          <textarea
            defaultValue={topic.story_md}
            className="story-content"
            style={{ minHeight: 160 }}
            onBlur={(e) => e.target.value !== topic.story_md && editStory(e.target.value)}
          />
        )}
      </div>

      <h2>
        <span className="step-badge">5</span> Publish learning content
      </h2>
      <p className="muted">
        Controls only the flashcards and story from step 4 above -- separate from publishing the
        assessment, which has its own publish button on the assessment editor page.
      </p>
      <div className="card row" style={{ justifyContent: "space-between" }}>
        <span>
          {topic.content_published ? (
            <span className="tag success">Flashcards + story live for students</span>
          ) : (
            <span className="tag general">Draft -- flashcards/story not visible to students yet</span>
          )}
        </span>
        <button className={topic.content_published ? "" : "primary"} onClick={togglePublish} disabled={publishBusy || approvedCount === 0}>
          {publishBusy ? "Working..." : topic.content_published ? "Unpublish" : "Publish learning content"}
        </button>
      </div>
      {approvedCount === 0 && <p className="muted">Approve at least one concept before publishing.</p>}

      <h2>
        <span className="step-badge">6</span> Assessment
      </h2>
      <p className="muted">
        Has its own publish step, independent of step 5 -- you can publish a test before or after
        publishing the flashcards/story, or without ever publishing them at all.
      </p>
      <Link to={`/coach/${id}/assessment`}>
        <button disabled={approvedCount === 0}>Go to assessment editor</button>
      </Link>
      {approvedCount === 0 && <p className="muted">Approve at least one concept first.</p>}
    </div>
  );
}
