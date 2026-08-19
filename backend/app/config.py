import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"

# Local, machine-specific CA bundle -- see README "Windows note (SSL)". Some
# antivirus/corporate setups (e.g. Norton's HTTPS scanning) MITM outbound TLS
# with their own certificate, which the default certifi bundle won't trust.
# If a coach has generated one (see README), pick it up automatically so
# `uvicorn app.main:app` works without having to export env vars by hand.
_local_ca_bundle = BACKEND_DIR / "combined_ca_bundle.pem"
if _local_ca_bundle.exists():
    os.environ.setdefault("SSL_CERT_FILE", str(_local_ca_bundle))
    os.environ.setdefault("REQUESTS_CA_BUNDLE", str(_local_ca_bundle))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env", extra="ignore")

    gemini_api_key: str = ""

    gemini_model: str = "gemini-3.5-flash"
    gemini_embedding_model: str = "gemini-embedding-001"
    # Gemini's native image model ("nano banana") -- used for the
    # kid-friendly concept illustrations, via generate_content with
    # response_modalities=["TEXT", "IMAGE"] rather than a separate Imagen call.
    gemini_image_model: str = "gemini-2.5-flash-image"

    google_client_id: str = ""
    google_client_secret: str = ""
    # The origin the browser actually addresses: the Vite dev server in local
    # dev (so the post-login redirect and Google's callback both land
    # somewhere that's actually serving the React app -- Vite's own proxy
    # forwards /api/* through to this backend either way), the Render URL in
    # production. Must exactly match a redirect URI registered in Google
    # Cloud Console.
    public_base_url: str = "http://localhost:5173"
    # Signs Starlette's SessionMiddleware cookie, which Authlib uses to stash
    # the OAuth state/nonce between the login and callback legs -- unrelated
    # to our own CoachSession cookie (app/auth.py), which is what actually
    # tracks "who's logged in" afterward.
    session_secret: str = "dev-insecure-secret-change-me"

    # Local SQLite by default (fine for dev). Production sets DATABASE_URL to
    # a managed Postgres (Neon) connection string -- local disk turned out to
    # not reliably persist on Render even on a paid plan, so the database no
    # longer lives there. Chroma (chroma_dir below) is unaffected by this --
    # it's a regenerable cache, not deliberately migrated off local disk.
    database_url: str = f"sqlite:///{DATA_DIR / 'sciolympiad.db'}"
    chroma_dir: str = str(DATA_DIR / "chroma")

    # Fernet key encrypting each coach's personal LLM API key at rest (see
    # app/crypto.py). Generate once with:
    #   python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
    # Empty = the per-coach "bring your own key" feature is disabled (coaches
    # can't save a personal key, but the shared Gemini key keeps working for
    # everyone -- this is purely additive, never required).
    credential_encryption_key: str = ""

    # Defaults for coaches who choose Claude or OpenAI as their personal
    # provider (app/llm/claude_adapter.py, app/llm/openai_adapter.py).
    # Unrelated to the gemini_* settings above, which back the shared
    # default key.
    claude_model: str = "claude-sonnet-5"
    openai_model: str = "gpt-4.1"
    openai_image_model: str = "gpt-image-1"

    # Retrieval tuning for the "don't over-index on video" behavior
    retrieval_top_k: int = 8
    relevance_threshold: float = 0.5


settings = Settings()
# Neon's dashboard shows a ready-to-paste `psql '...'` terminal command right
# next to the bare connection string -- easy to grab the wrong one when
# copying DATABASE_URL into Render. Strip that wrapper if present so a
# copy-paste mistake doesn't take down the whole deploy.
_url = settings.database_url.strip()
if _url.startswith("psql "):
    _url = _url[len("psql ") :].strip()
    if len(_url) >= 2 and _url[0] == _url[-1] and _url[0] in "'\"":
        _url = _url[1:-1]
    settings.database_url = _url
# Some providers (and older docs/examples) still hand back the legacy
# `postgres://` scheme; SQLAlchemy 2.0 rejects it outright. Normalize once
# here so every caller of settings.database_url gets a scheme it accepts.
if settings.database_url.startswith("postgres://"):
    settings.database_url = settings.database_url.replace("postgres://", "postgresql://", 1)
DATA_DIR.mkdir(parents=True, exist_ok=True)
