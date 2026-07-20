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
│   │   └── llm/               Gemini client wrapper + prompt templates
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
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

**Backend**

```sh
cd backend
python -m venv venv
venv\Scripts\activate        # Windows; use `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
copy .env.example .env       # then fill in GEMINI_API_KEY
uvicorn app.main:app --reload
```

> **Windows note:** `chromadb` depends on `chroma-hnswlib`, which as of this
> writing has no prebuilt wheel for Python 3.12 on Windows and needs the
> Microsoft C++ Build Tools to compile from source. Workaround: install a
> compatible prebuilt wheel first, then install chromadb without pulling its
> pinned version back in —
> `pip install chroma-hnswlib==0.7.5 --only-binary=:all:` followed by
> `pip install chromadb==0.5.23 --no-deps`, then `pip install -r
> requirements.txt` to fill in the rest (`pip check` will warn about the
> hnswlib version mismatch; it's harmless — Chroma runs fine on 0.7.5).
> Not needed on macOS/Linux, where a normal `pip install -r requirements.txt`
> just works.

> **Windows note (SSL):** If API calls fail with
> `[SSL: CERTIFICATE_VERIFY_FAILED] ... unable to get local issuer certificate`,
> your antivirus (Norton and some corporate security suites do this) is
> intercepting HTTPS with its own certificate, which Python's default trust
> bundle doesn't know about. Fix without touching any system/antivirus
> settings — export the antivirus's root cert and point Python at a bundle
> that includes it:
> ```powershell
> $cert = Get-ChildItem Cert:\LocalMachine\Root | Where-Object { $_.Subject -like '*Norton*' } | Select-Object -First 1
> $b64 = [System.Convert]::ToBase64String($cert.RawData, 'InsertLineBreaks')
> Set-Content backend\norton_root.pem "-----BEGIN CERTIFICATE-----`n$b64`n-----END CERTIFICATE-----`n" -Encoding ascii
> ```
> ```sh
> cat $(python -c "import certifi; print(certifi.where())") backend/norton_root.pem > backend/combined_ca_bundle.pem
> ```
> `app/config.py` picks up `backend/combined_ca_bundle.pem` automatically if
> present, so once it exists `uvicorn app.main:app --reload` just works. This
> file is machine-specific and gitignored — regenerate it per machine, and
> swap `*Norton*` for whatever antivirus/proxy is doing the intercepting if
> it's not Norton (check the "Issuer"/"OU" field on the invalid certificate).

Backend runs at `http://localhost:8000`. A demo topic ("Roller Coaster") is
seeded automatically on first run.

**Frontend**

```sh
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:5173`.

## Why Gemini for everything?

Every model call in this app — concept explanations, quiz generation,
relevance judging, hints, the tutor conversation, embeddings, and video/audio
transcription — goes through Gemini. One provider keeps setup to a single API
key, and Gemini's native multimodal input means uploaded video/audio can be
transcribed directly (no separate audio-extraction step). Every call is
routed through two small wrapper modules —
[`llm/client.py`](backend/app/llm/client.py) for generation and
[`rag/embeddings.py`](backend/app/rag/embeddings.py) /
[`rag/transcription.py`](backend/app/rag/transcription.py) for embeddings and
transcription — so swapping in a different provider (or splitting
generation/embeddings across two, as many production RAG apps do) is a
contained, one-file change.

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
   separate Gemini call scores it: "does this substantively explain a
   concept a student needs, or is it logistics/rules/off-topic?" This applies
   equally to video and text — it's the mechanism that keeps a video from
   dominating an explanation just because it exists, and it's what lets the
   coach UI show, per concept, whether video actually helped
   (`video coverage` tag) or the system fell back to general knowledge.

5. **Grounded generation**
   ([`llm/prompts.py`](backend/app/llm/prompts.py) `explanation_prompt`) —
   the surviving relevant chunks (labeled by source) are handed to Gemini,
   which is instructed to ground each concept explanation in them when
   possible and explicitly say so when it's using general knowledge instead.
   This is the "G" (generation) in RAG, and the source labeling is what makes
   the pipeline's behavior visible/auditable instead of a black box.

6. **Structured output** (`llm/client.py` `complete_json`) — several steps
   (relevance scores, the concept list, quiz questions) need machine-parseable
   output, not prose. These calls constrain Gemini's response to a JSON
   schema (`response_format`) instead of asking nicely and hoping the text
   parses.

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
- **Single LLM provider** — everything runs through Gemini; the `llm/client.py` / `rag/embeddings.py` / `rag/transcription.py` abstractions make splitting providers (e.g. a dedicated embeddings model) a contained, one-file change if needed later.
- **Approximate concept-to-resource attribution** — a concept's "video coverage" tag reflects whether *any* relevant retrieved chunk for the topic was a video, not a chunk-level citation per concept.

## Verification

Backend: `uvicorn app.main:app --reload` then `curl http://localhost:8000/api/health`.

Frontend: `npm run dev`, open `http://localhost:5173`, pick the seeded "Roller
Coaster" topic → Coach view → add a resource → generate explanations → approve
a couple → generate + publish an assessment → open Student view → take the
test → request a hint → answer one wrong on purpose → confirm the tutor chat
opens and responds.
