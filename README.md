# Science Olympiad Coach

A small RAG-powered app that helps a coach curate topics for a Science Olympiad
team, and helps students learn and practice them. Built as a portfolio piece
demonstrating applied RAG, embeddings, retrieval, grounded generation, and
LLM-driven tutoring — every piece is plain, readable code rather than hidden
behind a framework, so it doubles as a walkthrough of how these techniques fit
together.

**Coach flow:** log in → add a topic's resources (pasted text, a PDF, a
YouTube link, or any other URL — the system fetches/reads each one directly —
or an uploaded video/audio clip) → generate a concept glossary grounded in
whatever's actually useful in those resources → approve/edit it → let the
system suggest a mix of questions (you choose how many MCQ vs. short-answer)
and/or author your own questions by hand → publish.

**Student flow:** browse the concept glossary → take the assessment → ask for
hints → get a conversational, Socratic re-explanation on anything answered
wrong. No login required — students just enter a name per attempt.

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
│   │   ├── main.py          App wiring, session middleware, seeds a demo topic
│   │   ├── config.py        Settings (.env)
│   │   ├── auth.py           Coach password hashing + session cookies + require_coach dependency
│   │   ├── db.py, models.py, schemas.py   SQLite via SQLAlchemy
│   │   ├── routers/         auth, topics, ingestion, explain, assessment, attempts, tutor
│   │   ├── rag/               chunking, embeddings, vectorstore (Chroma), transcription,
│   │   │                      link_fetch, pdf_extract, youtube_fetch, retrieval
│   │   └── llm/                Gemini client wrapper (with per-call logging) + prompt templates
│   └── data/                  sqlite db + Chroma persistence (gitignored)
├── frontend/                  React + TypeScript (Vite)
│   └── src/
│       ├── api/client.ts      typed fetch wrapper for the backend
│       └── pages/              Login, Home, CoachTopicBuilder, CoachAssessment,
│                                StudentPractice, StudentTest
├── render.yaml                 Render deploy blueprint (see "Deploying" below)
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

**First-time setup (coach accounts).** There's no shared password to set —
coaches log in with individual accounts. The very first run shows a
"create the first coach account" screen right in the app; once you're logged
in, a small "Add a coach" card on the home page lets you create accounts for
teammates (you set their name + password and share it with them directly —
there's no self-serve signup or password reset, deliberately, for a ~13-person
known group). Students never log in at all.

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
   Before a retrieved chunk is allowed to influence an explanation, a single
   Gemini call scores every candidate chunk at once: "does this
   substantively explain a concept a student needs, or is it
   logistics/rules/off-topic?" This applies equally to video and text — it's
   the mechanism that keeps a video from dominating an explanation just
   because it exists, and it's what lets the coach UI show, per concept,
   whether video actually helped (`video coverage` tag) or the system fell
   back to general knowledge.

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

## Reducing AI/token usage

Not every step in this pipeline needs an LLM, and several that do were
originally calling it more than necessary. Four concrete things this codebase
does to keep AI use to what's actually needed:

1. **PDF, YouTube, and generic-link ingestion use zero LLM calls.** PDF text
   comes from [`pypdf`](backend/app/rag/pdf_extract.py) directly. YouTube
   transcripts come from the video's official caption track via
   [`youtube-transcript-api`](backend/app/rag/youtube_fetch.py) — no
   download, no transcription cost. Generic web pages go through
   [`trafilatura`](backend/app/rag/link_fetch.py)'s readable-content
   extractor. Only uploaded video/audio files (which have no existing
   transcript) actually need Gemini to transcribe them.
2. **Relevance judging is one call, not one per chunk.** Scoring up to
   `retrieval_top_k` candidate chunks used to be a separate LLM call each;
   [`rag/retrieval.py`](backend/app/rag/retrieval.py) now batches them into a
   single call that scores the whole set at once.
3. **Short-answer grading has a cheap pre-check.** Before spending an LLM
   call, [`routers/attempts.py`](backend/app/routers/attempts.py) normalizes
   and compares the student's answer to the correct answer; exact or
   near-exact matches are graded instantly with no LLM call. Only genuinely
   ambiguous phrasing falls through to the LLM grader.
4. **Regenerating concepts replaces, not duplicates.** Clicking "Generate
   concept explanations" again used to *add* another full set on top of the
   old one (wasting both the call and the resulting mess); it now clears the
   previous *unapproved* concepts first, so a coach can freely regenerate
   without piling up redundant LLM output (or duplicate rows).

**Visibility:** every LLM call goes through
[`llm/client.py`](backend/app/llm/client.py), which logs a labeled line
(`llm_call label=... effort=... input_chars=... output_chars=...`) for each
one. Watch the backend logs (locally, or Render's log tab once deployed) to
see exactly how many calls a given action costs.

## Simplifications (future work)

This is a small vertical slice, not a production app. Explicit corners cut:

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
- **One shared topic library** — every coach sees and can edit every topic;
  there's no per-team data isolation. That's a deliberate fit for one
  coaching staff, not a multi-tenant product.
- **Coach accounts have no password reset or self-service signup** — an
  existing coach creates every new account by hand and shares the password
  directly. Fine for a small known group; wouldn't scale past that.

## Further production hardening (not built, but worth knowing about)

Things a genuinely production-grade version of this would add, deliberately
left out here to keep this iteration's scope bounded:

- **Rate limiting / a per-coach cost budget** — nothing currently stops a
  coach from clicking "Generate" a hundred times in a row. The LLM-call
  logging (above) gives visibility, not a cap.
- **Automated database backups** — the SQLite file lives on Render's
  persistent disk, which survives redeploys but isn't backed up on a
  schedule. Worth a periodic manual export until this exists.
- **Structured monitoring/alerting** — logs exist (see "Reducing AI/token
  usage"), but nothing aggregates them or pages anyone if something breaks.
- **Password reset flow** — see above.
- **Postgres migration path** — `DATABASE_URL` already isolates the DB choice
  (see `app/config.py` / `app/db.py`), so moving off SQLite later is a
  connection-string change plus a data migration, not a rewrite — just not
  needed at ~13 users.

## Verification

Backend: `uvicorn app.main:app --reload` then `curl http://localhost:8000/api/health`.

Frontend: `npm run dev`, open `http://localhost:5173` → create the first coach
account (or log in) → pick the seeded "Roller Coaster" topic → Coach view →
add a resource (paste text, upload a PDF, paste a YouTube link, paste a plain
article link, or upload a video/audio clip) → generate explanations → approve
a couple → in the assessment editor, pick a mix of MCQ/short-answer and
generate, and/or add a question by hand → publish → open Student view (no
login needed) → take the test → request a hint → answer one wrong on purpose
→ confirm the tutor chat opens and responds.

## Deploying (so other coaches can use it)

This app is meant to be shared across the whole coaching team, not run only on
one laptop. It deploys as a **single service** — the FastAPI backend serves
both the API and the built frontend, so there's one URL to share and no CORS
to configure.

**One-time setup on [Render](https://render.com):**

1. Push this repo to GitHub (already done if you're reading this from the repo).
2. In Render: **New → Blueprint**, point it at this repo. It reads
   [`render.yaml`](render.yaml) and creates the web service automatically.
3. **Set the one secret** Render will prompt for (or add it under the
   service's **Environment** tab): `GEMINI_API_KEY` — your Gemini key.
4. Deploy. Render builds the frontend (`npm run build`) and installs the
   backend, then starts `uvicorn` behind Render's own HTTPS. Python version is
   pinned via [`.python-version`](.python-version) at the repo root — Render
   otherwise defaults to whatever its latest Python is, which can be too new
   to have prebuilt wheels for some of our dependencies (`pydantic-core`
   failed to build on Python 3.14 this way) and fails the build trying to
   compile them from source.
5. Open the deployed URL — it'll show "create the first coach account" since
   the database starts empty. Create your own account, then use the "Add a
   coach" card on the home page to create one for each other coach and share
   their password with them directly.

**Persistent data.** `render.yaml` provisions a small disk mounted at
`backend/data`, where the SQLite database and the Chroma vector store live —
without it, all topics/resources/concepts would reset on every redeploy.
That requires Render's `starter` plan (a few dollars/month), which is what
`render.yaml` specifies; the free tier has no persistent disk. If you just
want a quick smoke-test deploy first, you can temporarily drop the `disk:`
block and use the free plan — just know a redeploy will wipe the data.

**Updating the deployment:** push to `main` — Render auto-deploys on every
push to the branch the Blueprint was created from.
