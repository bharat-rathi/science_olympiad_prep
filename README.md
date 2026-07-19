# Science Olympiad Coach

A small RAG-powered app that helps a coach curate topics for a Science Olympiad
team, and helps students learn and practice them. Built as a portfolio piece
demonstrating applied RAG, embeddings, retrieval, grounded generation, and
LLM-driven tutoring — every piece is plain, readable code rather than hidden
behind a framework, so it doubles as a walkthrough of how these techniques fit
together.

**Coach flow:** add a topic's resources (pasted text/links, or an uploaded
video/audio clip) → generate a concept glossary grounded in whatever's
actually useful in those resources → approve/edit it → generate a practice
assessment → publish it.

**Student flow:** browse the concept glossary → take the assessment → ask for
hints → get a conversational, Socratic re-explanation on anything answered
wrong.

## Why this exists

Science Olympiad prep usually means a coach manually explaining jargon and
building quizzes by hand, and a video of an official explaining a topic that
may or may not actually be a good teaching resource. This app treats video as
*one possible source among several* rather than the backbone of every
explanation — a relevance-judging step (see below) decides, per topic, whether
the team's video coverage is actually useful, and falls back to general
knowledge when it isn't.

## Architecture

```
sciolympiad-coach/
├── backend/                 FastAPI (Python)
│   ├── app/
│   │   ├── main.py          App wiring, CORS, seeds a demo topic
│   │   ├── config.py        Settings (.env)
│   │   ├── db.py, models.py, schemas.py   SQLite via SQLAlchemy
│   │   ├── routers/         topics, ingestion, explain, assessment, attempts, tutor
│   │   ├── rag/              chunking, embeddings, vectorstore (Chroma), transcription, retrieval
│   │   └── llm/               Anthropic client wrapper + prompt templates
│   └── data/                 sqlite db + Chroma persistence (gitignored)
├── frontend/                 React + TypeScript (Vite)
│   └── src/
│       ├── api/client.ts     typed fetch wrapper for the backend
│       └── pages/             CoachTopicBuilder, CoachAssessment, StudentPractice, StudentTest
└── README.md (this file)
```

## Setup

**Prerequisites**
- Python 3.11+
- Node.js 18+
- [ffmpeg](https://ffmpeg.org/download.html) on your `PATH` — only needed if
  you want to upload video/audio resources (extracts audio before sending it
  to Whisper). Everything else works without it.
- An Anthropic API key and an OpenAI API key (see below for what each is used for)

**Backend**

```sh
cd backend
python -m venv venv
venv\Scripts\activate        # Windows; use `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
copy .env.example .env       # then fill in ANTHROPIC_API_KEY and OPENAI_API_KEY
uvicorn app.main:app --reload
```

Backend runs at `http://localhost:8000`. A demo topic ("Roller Coaster") is
seeded automatically on first run.

**Frontend**

```sh
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Why two LLM providers?

- **Anthropic (Claude)** does every reasoning/generation step: judging chunk
  relevance, writing concept explanations, generating quiz questions,
  grading short answers, hints, and the tutor conversation. One place to swap
  models: `backend/app/llm/client.py`.
- **OpenAI** is used *only* for embeddings (`text-embedding-3-small`, used for
  retrieval) and Whisper transcription of uploaded video/audio — Anthropic
  doesn't offer an embeddings API, and this was the simplest way to get both
  without adding a third provider.

## Concepts you'll see in this codebase

A few applied-AI ideas show up as small, concrete pieces of code rather than
abstract theory. Reading these in order roughly follows the pipeline:

1. **Chunking** ([`rag/chunking.py`](backend/app/rag/chunking.py)) — long text
   (a transcript, a pasted article) is split into overlapping ~500-token
   windows. Overlap exists so a concept that straddles a chunk boundary isn't
   lost in either half.

2. **Embeddings** ([`rag/embeddings.py`](backend/app/rag/embeddings.py)) —
   each chunk is turned into a vector such that semantically similar text ends
   up with similar vectors. This is what lets retrieval work by *meaning*
   rather than keyword matching.

3. **Vector storage & retrieval**
   ([`rag/vectorstore.py`](backend/app/rag/vectorstore.py)) — chunks and their
   embeddings are stored in [Chroma](https://www.trychroma.com/), a small
   local vector database, tagged with which topic and resource they came
   from. At query time we embed the topic's name+description and pull the
   most similar chunks — this is the "R" (retrieval) in RAG.

4. **Relevance judging** — *the "don't over-index on video" step*
   ([`rag/retrieval.py`](backend/app/rag/retrieval.py)). Similarity search
   alone will always return *something*, even if it's not actually useful.
   Before a retrieved chunk is allowed to influence an explanation, a
   separate Claude call scores it: "does this substantively explain a
   concept a student needs, or is it logistics/rules/off-topic?" This applies
   equally to video and text — it's the mechanism that keeps a video from
   dominating an explanation just because it exists, and it's what lets the
   coach UI show, per concept, whether video actually helped
   (`video coverage` tag) or the system fell back to general knowledge.

5. **Grounded generation**
   ([`llm/prompts.py`](backend/app/llm/prompts.py) `explanation_prompt`) —
   the surviving relevant chunks (labeled by source) are handed to Claude,
   which is instructed to ground each concept explanation in them when
   possible and explicitly say so when it's using general knowledge instead.
   This is the "G" (generation) in RAG, and the source labeling is what makes
   the pipeline's behavior visible/auditable instead of a black box.

6. **Structured output** (`llm/client.py` `complete_json`) — several steps
   (relevance scores, the concept list, quiz questions) need machine-parseable
   output, not prose. These calls constrain Claude's response to a JSON
   schema (`output_config.format`) instead of asking nicely and hoping the
   text parses.

7. **Grounded conversation** (`routers/tutor.py`, `llm/prompts.py`
   `tutor_system_prompt`) — when a student answers wrong, the tutor chat isn't
   a generic chatbot: its system prompt is built from the *same approved
   concept explanation* the coach curated, plus the specific question and the
   student's wrong answer, so the conversation stays grounded and Socratic
   rather than just restating the answer.

## Simplifications (future work)

This is a single vertical slice, not a production app. Explicit corners cut:

- **No auth/accounts** — one shared coach view; students just type a name per attempt.
- **No live web search** for outside resources — a coach pastes text/links manually.
- **Local-only** — SQLite + local Chroma directory, run with `uvicorn`/`vite dev`; no deployment config.
- **Single LLM provider for generation** — Gemini isn't wired in, though the `llm/client.py` abstraction makes that a small, contained change.
- **Approximate concept-to-resource attribution** — a concept's "video coverage" tag reflects whether *any* relevant retrieved chunk for the topic was a video, not a chunk-level citation per concept.

## Verification

Backend: `uvicorn app.main:app --reload` then `curl http://localhost:8000/api/health`.

Frontend: `npm run dev`, open `http://localhost:5173`, pick the seeded "Roller
Coaster" topic → Coach view → add a resource → generate explanations → approve
a couple → generate + publish an assessment → open Student view → take the
test → request a hint → answer one wrong on purpose → confirm the tutor chat
opens and responds.
