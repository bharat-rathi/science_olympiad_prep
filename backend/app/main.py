from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import models
from app.db import SessionLocal, engine
from app.routers import assessment, attempts, explain, ingestion, topics, tutor

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Science Olympiad Coach")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(topics.router)
app.include_router(ingestion.router)
app.include_router(explain.router)
app.include_router(assessment.router)
app.include_router(attempts.router)
app.include_router(tutor.router)


@app.on_event("startup")
def seed_demo_topic() -> None:
    db = SessionLocal()
    try:
        exists = db.query(models.Topic).filter(models.Topic.name == "Roller Coaster").first()
        if not exists:
            db.add(
                models.Topic(
                    event_name="Roller Coaster",
                    name="Roller Coaster",
                    description=(
                        "Division B/C event: teams design and build a roller coaster that "
                        "transports a marble/ball through a course, applying concepts of "
                        "energy conservation, forces, and track design."
                    ),
                )
            )
            db.commit()
    finally:
        db.close()


@app.get("/api/health")
def health():
    return {"status": "ok"}
