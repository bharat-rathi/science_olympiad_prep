# Science Olympiad Coach

A small RAG-powered app that helps a coach curate topics for a Science Olympiad
team, and helps students learn and practice them. Built as a portfolio piece
demonstrating applied RAG, embeddings, retrieval, grounded generation, and
LLM-driven tutoring — every piece is plain, readable code rather than hidden
behind a framework, so it doubles as a walkthrough of how these techniques fit
together.

**Coach flow:** add a topic's resources (pasted text, a real URL the system
fetches and reads directly, or an uploaded video/audio clip) → generate a
concept glossary grounded in whatever's actually useful in those resources →
approve/edit it → generate a practice assessment → publish it.

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
│   │   ├── rag/              chunking, embeddings, vectorstore (Chroma), transcription, link_fetch, retrieval
│   │   └── llm/               Gemini client wrapper + prompt templates
│   └── data/                 sqlite db + Chroma persistence (gitignored)
├── frontend/                 React + TypeScript (Vite)
│   └── src/
│       ├── api/client.ts     typed fetch wrapper for the backend
│       └── pages/             CoachTopicBuilder, CoachAssessment, StudentPractice, StudentTest
├── render.yaml                Render deploy blueprint (see "Deploying" below)
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
   (a transcript, a pasted article, or a URL's extracted content — see
   [`rag/link_fetch.py`](backend/app/rag/link_fetch.py)) is split into
   overlapping ~500-token windows. Overlap exists so a concept that straddles
   a chunk boundary isn't lost in either half.

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

This is a small vertical slice, not a production app. Explicit corners cut:

- **One shared password, not per-coach accounts** — good enough to keep the app
  private to your ~13 coaches, but there's no notion of *who* curated or
  approved what. Students just type a name per attempt, no login at all.
- **No general web search** — a coach still has to know and paste the specific
  URL they want ingested; the system doesn't go find sources on its own.
- **Single LLM provider** — everything runs through Gemini; the `llm/client.py`
  / `rag/embeddings.py` / `rag/transcription.py` abstractions make splitting
  providers (e.g. a dedicated embeddings model) a contained, one-file change
  if needed later.
- **Approximate concept-to-resource attribution** — a concept's "video
  coverage" tag reflects whether *any* relevant retrieved chunk for the topic
  was a video, not a chunk-level citation per concept.
- **SQLite + local-disk Chroma**, not a managed database — fine at this scale
  (one small Render instance, ~13 users), but it means the app can only ever
  run as a single instance/replica; it wouldn't survive being scaled
  horizontally without moving to Postgres/pgvector or similar.

## Verification

Backend: `uvicorn app.main:app --reload` then `curl http://localhost:8000/api/health`.

Frontend: `npm run dev`, open `http://localhost:5173`, pick the seeded "Roller
Coaster" topic → Coach view → add a resource (paste text, paste a real link,
or upload a clip) → generate explanations → approve a couple → generate +
publish an assessment → open Student view → take the test → request a hint →
answer one wrong on purpose → confirm the tutor chat opens and responds.

## Deploying (so other coaches can use it)

This app is meant to be shared across the whole coaching team, not run only on
one laptop. It deploys as a **single service** — the FastAPI backend serves
both the API and the built frontend, so there's one URL to share and no CORS
to configure.

**One-time setup on [Render](https://render.com):**

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. In Render: **New → Blueprint**, point it at this repo. It reads
   [`render.yaml`](render.yaml) and creates the web service automatically.
3. **Set the two secrets** Render will prompt for (or add them under the
   service's **Environment** tab):
   - `GEMINI_API_KEY` — your Gemini key.
   - `COACH_PASSWORD` — one password you'll share with the other coaches.
     Leaving this unset (as in local dev) disables the login gate entirely —
     don't leave it unset on a public deployment.
4. Deploy. Render builds the frontend (`npm run build`) and installs the
   backend, then starts `uvicorn` behind Render's own HTTPS.
5. Share the resulting `https://sciolympiad-coach.onrender.com`-style URL and
   the `COACH_PASSWORD` with your other coaches — that's the whole onboarding
   step, since it's one shared login rather than individual accounts.

**Persistent data.** `render.yaml` provisions a small disk mounted at
`backend/data`, where the SQLite database and the Chroma vector store live —
without it, all topics/resources/concepts would reset on every redeploy.
That requires Render's `starter` plan (a few dollars/month), which is what
`render.yaml` specifies; the free tier has no persistent disk. If you just
want a quick smoke-test deploy first, you can temporarily drop the `disks:`
block and use the free plan — just know a redeploy will wipe the data.

**Updating the deployment:** push to `main` — Render auto-deploys on every
push to the branch the Blueprint was created from.
