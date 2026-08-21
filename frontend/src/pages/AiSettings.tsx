import { useEffect, useState } from "react";
import { api, AiSettings as AiSettingsType, DriveStatus } from "../api/client";

const PROVIDER_LABELS: Record<string, string> = {
  gemini: "Gemini",
  claude: "Claude",
  openai: "OpenAI",
};

export default function AiSettings() {
  const [settings, setSettings] = useState<AiSettingsType | null>(null);
  const [provider, setProvider] = useState<AiSettingsType["provider"]>(null);
  const [apiKey, setApiKey] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  const [driveStatus, setDriveStatus] = useState<DriveStatus | null>(null);
  const [disconnectingDrive, setDisconnectingDrive] = useState(false);

  useEffect(() => {
    api.getAiSettings().then((s) => {
      setSettings(s);
      setProvider(s.provider);
    });
    api.getDriveStatus().then(setDriveStatus);
  }, []);

  async function disconnectDrive() {
    setDisconnectingDrive(true);
    try {
      setDriveStatus(await api.disconnectDrive());
    } finally {
      setDisconnectingDrive(false);
    }
  }

  async function save() {
    setError("");
    setMessage("");
    if (provider && !apiKey.trim()) {
      setError("Enter an API key for that provider first.");
      return;
    }
    setSaving(true);
    try {
      const updated = await api.updateAiSettings({ provider, api_key: provider ? apiKey.trim() : null });
      setSettings(updated);
      setApiKey("");
      setMessage(provider ? `Saved -- your ${PROVIDER_LABELS[provider]} key is now in use.` : "Reverted to the team's shared key.");
    } catch (err) {
      setError(err instanceof Error ? err.message : String(err));
    } finally {
      setSaving(false);
    }
  }

  if (!settings) return <p>Loading...</p>;

  return (
    <div>
      <div className="page-header">
        <h1>AI Settings</h1>
        <p className="muted">
          Choose your own AI provider and bring your own API key for explanations, story generation, quiz
          questions, and other content you generate. If you don't set one, everything uses the team's shared
          key -- this is entirely optional.
        </p>
      </div>

      <div className="card stack">
        <span>
          {settings.has_key ? (
            <span className="tag success">Using your {PROVIDER_LABELS[settings.provider ?? ""] ?? ""} key</span>
          ) : (
            <span className="tag general">Using the team's shared key</span>
          )}
        </span>

        <label className="muted">Provider</label>
        <select
          value={provider ?? ""}
          onChange={(e) => setProvider((e.target.value || null) as AiSettingsType["provider"])}
        >
          <option value="">Use team default (Gemini)</option>
          <option value="gemini">Gemini</option>
          <option value="claude">Claude</option>
          <option value="openai">OpenAI</option>
        </select>

        {provider && (
          <>
            <label className="muted">{PROVIDER_LABELS[provider]} API key</label>
            <input
              type="password"
              placeholder={settings.provider === provider && settings.has_key ? "Enter a new key to replace the saved one" : "Paste your API key"}
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
            />
          </>
        )}

        {error && <p style={{ color: "var(--danger)" }}>{error}</p>}
        {message && <p className="muted">{message}</p>}

        <div className="row">
          <button className="primary" onClick={save} disabled={saving}>
            {saving ? "Saving..." : "Save"}
          </button>
        </div>

        <p className="muted" style={{ marginTop: 8 }}>
          Note: video/audio transcription always uses the team's shared Gemini key, regardless of this
          setting -- Claude and OpenAI don't support that directly. Claude also has no image-generation API,
          so flashcard images fall back to the shared key when Claude is selected.
        </p>
      </div>

      <div className="card stack" style={{ marginTop: 24 }}>
        <h2 style={{ margin: 0 }}>Google Drive</h2>
        <p className="muted" style={{ margin: 0 }}>
          Connect Google Drive to add a video straight from a share link when adding resources to a topic --
          same as pasting a YouTube link. Optional; only needed if you have videos on Drive.
        </p>
        {driveStatus && (
          <>
            <span>
              {driveStatus.connected ? (
                <span className="tag success">Connected</span>
              ) : (
                <span className="tag general">Not connected</span>
              )}
            </span>
            <div className="row">
              {driveStatus.connected ? (
                <button onClick={disconnectDrive} disabled={disconnectingDrive}>
                  {disconnectingDrive ? "Disconnecting..." : "Disconnect"}
                </button>
              ) : (
                <button className="primary" onClick={() => (window.location.href = "/api/auth/google/drive/connect")}>
                  Connect Google Drive
                </button>
              )}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
