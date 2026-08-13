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

  const [expandedResourceIds, setExpandedResourceIds] = useState<Set<number>>(new Set());

  const [feedbackDrafts, setFeedbackDrafts] = useState<Record<number, string>>({});
  const [refiningId, setRefiningId] = useState<number | null>(null);
  const [imagingId, setImagingId] = useState<number | null>(null);
  const [storyBusy, setStoryBusy] = useState(false);
  const [publishBusy, setPublishBusy] = useState(false);

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

  function toggleResourceExpand(resourceId: number) {
    setExpandedResourceIds((prev) => {
      const next = new Set(prev);
      if (next.has(resourceId)) next.delete(resourceId);
      else next.add(resourceId);
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

  async function editAnalogy(c: ConceptTerm, analogy: string) {
    const updated = await api.updateConcept(id, c.id, { analogy });
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
            <input
              type="file"
              accept=".mp4,.mov,.mkv,.avi,.webm,.mp3,.wav,.m4a,.flac,.pdf,.zip"
              onChange={uploadFile}
              disabled={busy}
            />
          </label>
        </div>
      </div>

      <div className="card stack">
        <label className="muted">
          Or paste a link -- YouTube links pull the official captions, anything else gets its
          readable text fetched directly. No link handy? Type a topic or keyword instead and the
          research agent will search the web and summarize what it finds.
        </label>
        <div className="row">
          <input
            placeholder="https://... or a topic keyword"
            value={linkUrl}
            onChange={(e) => setLinkUrl(e.target.value)}
            style={{ flex: 1 }}
          />
          <button className="primary" onClick={addLink} disabled={linkBusy}>
            {linkBusy ? "Working..." : "Fetch / research & add"}
          </button>
        </div>
        {linkError && <p style={{ color: "var(--danger)" }}>{linkError}</p>}
      </div>

      {resources.length > 0 && (
        <div className="stack">
          {resources.map((r) => {
            const content = r.type === "video" ? r.transcript : r.raw_text;
            const isExpanded = expandedResourceIds.has(r.id);
            return (
              <div className="card" key={r.id}>
                <div className="row" style={{ justifyContent: "space-between" }}>
                  <span>
                    <span className={`tag ${r.type === "video" ? "video" : r.type === "research" ? "general" : ""}`}>
                      {r.type}
                    </span>
                    {r.title}
                  </span>
                  {content && (
                    <button onClick={() => toggleResourceExpand(r.id)}>
                      {isExpanded ? "Hide content" : "View content"}
                    </button>
                  )}
                </div>
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

      <h2>
        <span className="step-badge">2</span> Concept explanations
      </h2>
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
            <label className="muted" style={{ marginTop: 4 }}>
              Explanation
            </label>
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
            <div className="row" style={{ alignItems: "flex-start" }}>
              {c.image_data_url && (
                <img src={c.image_data_url} alt={c.term} className="concept-image-preview" />
              )}
              <button onClick={() => generateImage(c)} disabled={imagingId === c.id}>
                {imagingId === c.id ? "Drawing..." : c.image_data_url ? "Regenerate image" : "Generate image"}
              </button>
            </div>
            <div className="row">
              <label className="row">
                <input type="checkbox" checked={c.approved} onChange={() => toggleApprove(c)} />
                Approved (used for both flashcards and assessment questions)
              </label>
            </div>
          </div>
        ))}
      </div>

      <h2>
        <span className="step-badge">3</span> Story (optional)
      </h2>
      <p className="muted">
        Weaves the approved concepts into one short narrative students can read as a story instead
        of a list of definitions. Only generated when you ask for it.
      </p>
      <div className="card stack">
        <button onClick={generateStory} disabled={storyBusy || approvedCount === 0}>
          {storyBusy ? "Writing..." : topic.story_md ? "Regenerate story" : "Generate story"}
        </button>
        {approvedCount === 0 && <p className="muted">Approve at least one concept first.</p>}
        {topic.story_md && (
          <textarea
            defaultValue={topic.story_md}
            style={{ minHeight: 160 }}
            onBlur={(e) => e.target.value !== topic.story_md && editStory(e.target.value)}
          />
        )}
      </div>

      <h2>
        <span className="step-badge">4</span> Publish learning content
      </h2>
      <p className="muted">
        Controls only the flashcards and story from step 3 above -- separate from publishing the
        assessment, which has its own publish button on the assessment editor page.
      </p>
      <div className="card row" style={{ justifyContent: "space-between" }}>
        <span>
          {topic.content_published ? (
            <span className="tag video">Flashcards + story live for students</span>
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
        <span className="step-badge">5</span> Assessment
      </h2>
      <p className="muted">
        Has its own publish step, independent of step 4 -- you can publish a test before or after
        publishing the flashcards/story, or without ever publishing them at all.
      </p>
      <Link to={`/coach/${id}/assessment`}>
        <button disabled={approvedCount === 0}>Go to assessment editor</button>
      </Link>
      {approvedCount === 0 && <p className="muted">Approve at least one concept first.</p>}
    </div>
  );
}
