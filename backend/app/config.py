from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BACKEND_DIR / "data"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BACKEND_DIR / ".env", extra="ignore")

    anthropic_api_key: str = ""
    openai_api_key: str = ""

    anthropic_model: str = "claude-sonnet-5"
    openai_embedding_model: str = "text-embedding-3-small"
    openai_transcribe_model: str = "whisper-1"

    database_url: str = f"sqlite:///{DATA_DIR / 'sciolympiad.db'}"
    chroma_dir: str = str(DATA_DIR / "chroma")

    # Retrieval tuning for the "don't over-index on video" behavior
    retrieval_top_k: int = 8
    relevance_threshold: float = 0.5


settings = Settings()
DATA_DIR.mkdir(parents=True, exist_ok=True)
