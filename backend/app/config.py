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

    # Shared password gating the whole app now that ~13 coaches access one
    # deployed instance. Empty string (the local-dev default) disables the
    # gate entirely -- only set this in the hosted deployment's env vars.
    coach_password: str = ""

    database_url: str = f"sqlite:///{DATA_DIR / 'sciolympiad.db'}"
    chroma_dir: str = str(DATA_DIR / "chroma")

    # Retrieval tuning for the "don't over-index on video" behavior
    retrieval_top_k: int = 8
    relevance_threshold: float = 0.5


settings = Settings()
DATA_DIR.mkdir(parents=True, exist_ok=True)
