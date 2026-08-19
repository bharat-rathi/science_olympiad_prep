from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

# check_same_thread is SQLite-only (needed because FastAPI's dependency-
# injected session can cross threads via the threadpool) -- psycopg2 doesn't
# accept it and raises TypeError if passed, so only apply it for SQLite.
connect_args = {"check_same_thread": False} if settings.database_url.startswith("sqlite") else {}
# pool_pre_ping: serverless Postgres (Neon) aggressively recycles idle pooled
# connections server-side. Without this, the first query on a connection the
# pool thinks is still good but Neon has already closed fails with
# "server closed the connection unexpectedly" -- pre_ping issues a cheap
# liveness check before handing a pooled connection out and transparently
# reconnects if it's gone. Harmless no-op cost for SQLite.
engine = create_engine(settings.database_url, connect_args=connect_args, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
