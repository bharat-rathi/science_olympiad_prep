import { useEffect, useState } from "react";
import { api, TopicChatMessage } from "../api/client";
import { getOrCreateSessionToken } from "../lib/sessionToken";

export default function TopicChat({ topicId }: { topicId: number }) {
  const [messages, setMessages] = useState<TopicChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    setLoaded(false);
    // Coaches are identified by their session cookie server-side; the token
    // is only used when there's no coach in that cookie (an anonymous
    // student), but it's cheap to always send.
    api.getTopicChat(topicId, getOrCreateSessionToken()).then((msgs) => {
      setMessages(msgs);
      setLoaded(true);
    });
  }, [topicId]);

  async function send() {
    if (!input.trim() || busy) return;
    const text = input;
    setInput("");
    const userMsg: TopicChatMessage = { id: -1, role: "user", content: text, created_at: "" };
    setMessages((prev) => [...prev, userMsg]);
    setBusy(true);
    try {
      const reply = await api.topicChatTurn(topicId, text, getOrCreateSessionToken());
      setMessages((prev) => [...prev, reply]);
    } finally {
      setBusy(false);
    }
  }

  return (
    <div className="card">
      {loaded && messages.length === 0 && (
        <p className="muted" style={{ margin: "0 0 10px" }}>
          Ask anything about this topic's uploaded material -- answers are grounded in what's been added below.
        </p>
      )}
      <div className="chat-thread">
        {messages.map((m, i) => (
          <div key={i} className={`chat-bubble ${m.role}`}>
            {m.content}
          </div>
        ))}
      </div>
      <div className="row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && send()}
          placeholder="Ask a question about this content..."
          disabled={busy}
        />
        <button className="primary" onClick={send} disabled={busy}>
          {busy ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
}
