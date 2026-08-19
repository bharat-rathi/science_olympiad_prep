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
│   │   ├── auth.py           Google OAuth registry + session cookies + require_coach dependency
│   │   ├── db.py, models.py, schemas.py   SQLAlchemy -- Postgres (Neon) in production,
│   │   │                                  local SQLite by default for dev (DATABASE_URL)
│   │   ├── routers/         auth, topics, ingestion, explain, assessment, attempts, tutor
│   │   ├── rag/               chunking, embeddings, vectorstore (Chroma), transcription,
│   │   │                      link_fetch, pdf_extract, youtube_fetch, retrieval
│   │   └── llm/                Gemini client wrapper (with per-call logging) + prompt templates
│   └── data/                  Chroma persistence (gitignored) -- local SQLite db too, in dev
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
- A Google OAuth client (for coach sign-in) — see the next section

**Google Cloud Console setup (one-time, for coach sign-in)**

Coaches authenticate with "Sign in with Google," which needs an OAuth client
you create yourself (this app never sees your Google account credentials —
it only receives an email/name/id token back from Google after you approve
the sign-in):

1. Go to [console.cloud.google.com](https://console.cloud.google.com/) →
   create a project (or reuse one) — e.g. "Science Olympiad Coach".
2. **APIs & Services → OAuth consent screen**:
   - User type: **External**.
   - App name, support email — anything reasonable.
   - Scopes: leave the defaults (`openid`, `email`, `profile` — no sensitive
     scopes needed).
   - Publishing status: leave it as **Testing** rather than publishing —
     avoids Google's app-verification review, which isn't worth it for a
     ~13-person tool. The tradeoff: while in Testing, Google *itself* only
     allows sign-in for emails you've added under **Test users** on this
     same screen — so every coach's email needs to be added **here**, in
     addition to being invited from inside the app (the "Invite a coach"
     card on the home page). Two lists, same people.
3. **APIs & Services → Credentials → Create Credentials → OAuth client ID**:
   - Application type: **Web application**.
   - **Authorized redirect URIs** — add both:
     - `http://localhost:5173/api/auth/google/callback` (local dev)
     - `https://<your-render-url>/api/auth/google/callback` (production —
       use the actual `.onrender.com` URL from your Render dashboard)
   - Create, then copy the **Client ID** and **Client secret**.
4. Put those in `backend/.env` as `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET`
   for local dev, and in the Render service's **Environment** tab for
   production (see "Deploying" below).

**Backend**

```sh
cd backend
python -m venv venv
venv\Scripts\activate        # Windows; use `source venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
copy .env.example .env       # then fill in GEMINI_API_KEY, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, SESSION_SECRET
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

**First-time setup (coach accounts).** Coaches sign in with Google — no
passwords to set or share. You'll need Google OAuth credentials first (see
"Google Cloud Console setup" below); once `GOOGLE_CLIENT_ID`/
`GOOGLE_CLIENT_SECRET` are in `backend/.env`, the very first sign-in creates
the first coach account automatically. After that, a small "Invite a coach"
card on the home page lets you add teammates by email — only invited emails
can complete Google sign-in and get an account (there's no open self-serve
signup, deliberately, for a ~13-person known group). Students never log in
at all.

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
- **Local-disk Chroma**, not a managed vector store — fine at this scale (one
  small Render instance, ~13 users); it means the app can only ever run as a
  single instance/replica, and Chroma's index doesn't survive a disk hiccup
  (though it's a regenerable cache of resource text, not source-of-truth
  data — see "Postgres migration" below for why that distinction mattered).
  Moving it to a hosted vector store would be needed to scale horizontally.
- **One shared topic library** — every coach sees and can edit every topic;
  there's no per-team data isolation. That's a deliberate fit for one
  coaching staff, not a multi-tenant product.
- **No self-service signup** — an existing coach invites every new account by
  email; only that email can complete Google sign-in. There's no password to
  reset (Google handles the actual authentication), but the invite step is
  manual by design. Fine for a small known group; wouldn't scale past that.
- **Google OAuth consent screen stays in "Testing" mode** — avoids Google's
  app-verification review, but means every coach's email has to be added
  twice: once as an invite in this app, once as a Google "Test user" in
  Cloud Console. Publishing the OAuth app removes that duplication but adds
  Google's review process — not worth it at this scale.

## Further production hardening (not built, but worth knowing about)

Things a genuinely production-grade version of this would add, deliberately
left out here to keep this iteration's scope bounded:

- **Rate limiting / a per-coach cost budget** — nothing currently stops a
  coach from clicking "Generate" a hundred times in a row. The LLM-call
  logging (above) gives visibility, not a cap.
- **Automated database backups** — the database is now Neon Postgres (see
  "Database (Neon Postgres)" below), which has its own point-in-time-recovery
  story, but the **free tier's retention window is short**. Worth confirming
  Neon's current free-tier retention and/or upgrading if this data ever
  becomes hard to lose again.
- **Structured monitoring/alerting** — logs exist (see "Reducing AI/token
  usage"), but nothing aggregates them or pages anyone if something breaks.

## Database (Neon Postgres)

Production data used to live in a SQLite file on Render's persistent disk.
That disk turned out not to actually persist across deploys even on a paid
plan (confirmed in the Render dashboard) — every redeploy silently started
the app against an empty database. The database now lives in a separate,
managed Postgres instance on [Neon](https://neon.tech) instead, which
persists independently of anything happening to the Render service. Chroma
(the vector store) is unaffected by this — it's still local disk, since it's
a regenerable cache, not irreplaceable data (see "Simplifications" above).

Local dev is unaffected either way — `DATABASE_URL` is optional and defaults
to a local SQLite file (see `backend/.env.example`) unless you deliberately
set it to test against Postgres too.

**One-time setup, for whoever is standing up (or re-pointing) this app:**

1. Go to [neon.tech](https://neon.tech), sign up (GitHub or Google both
   work), and create a new project. Neon's default database name (`neondb`)
   is fine — nothing in this app depends on the name.
2. On the project's dashboard, open **Connection Details** and copy the
   **Pooled connection** string — the app makes one connection per request
   via `SessionLocal`/`get_db`, which is exactly what pooled connections are
   for. It looks like:
   `postgresql://<user>:<password>@<host>-pooler.<region>.aws.neon.tech/<dbname>?sslmode=require`
3. Set that string as `DATABASE_URL`:
   - **Locally**, in `backend/.env`, if you want to test against real
     Postgres before deploying a schema change.
   - **On Render**, in the dashboard → this service → **Environment** tab —
     add it there directly. (`render.yaml` also lists `DATABASE_URL`, but
     this service isn't Blueprint-synced, so editing `render.yaml` alone
     does **not** change the live service — the dashboard entry is the one
     that actually matters.)
4. No manual schema setup needed in Neon's SQL editor — the app's existing
   `create_all()` + `_ensure_column` migration pattern (see `app/main.py`)
   builds the schema on first boot against whatever `DATABASE_URL` points
   to, the same way it always has for SQLite.

Use a **separate Neon project for local testing** vs. the one you point
production at, so poking around locally never risks the real data.

## Verification

Backend: `uvicorn app.main:app --reload` then `curl http://localhost:8000/api/health`.

Frontend: `npm run dev`, open `http://localhost:5173` → sign in with Google
(creates the first coach account automatically if none exist yet) → pick the
seeded "Roller Coaster" topic → Coach view →
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
3. **Set the secrets** Render will prompt for (or add them under the
   service's **Environment** tab): `GEMINI_API_KEY`, `GOOGLE_CLIENT_ID`,
   `GOOGLE_CLIENT_SECRET`, `SESSION_SECRET`, `DATABASE_URL` (a Neon Postgres
   connection string — see "Database (Neon Postgres)" below) (see "Google
   Cloud Console setup" above for the Google values — make sure the OAuth
   client's authorized redirect URIs include this service's actual
   `.onrender.com` URL). `PUBLIC_BASE_URL` is already set in `render.yaml`
   to this repo's known Render URL; update it there (or override in the
   dashboard) if yours differs.
4. Deploy. Render builds the frontend (`npm run build`) and installs the
   backend, then starts `uvicorn` behind Render's own HTTPS. Python version is
   pinned via [`.python-version`](.python-version) at the repo root — Render
   otherwise defaults to whatever its latest Python is, which can be too new
   to have prebuilt wheels for some of our dependencies (`pydantic-core`
   failed to build on Python 3.14 this way) and fails the build trying to
   compile them from source.
5. Open the deployed URL and sign in with Google — the first sign-in creates
   the first coach account automatically since the database starts empty.
   From there, use the "Invite a coach" card on the home page to invite each
   teammate by email (and remember to also add them as a Google Test user —
   see "Google Cloud Console setup" above).

**Persistent data.** The actual database (coaches, topics, resources,
concepts, assessments, attempts) lives in Neon Postgres via `DATABASE_URL` —
see "Database (Neon Postgres)" above — not on Render's disk. This matters:
an earlier version of this app stored everything in a SQLite file on
Render's disk instead, and that disk turned out not to reliably persist
across deploys even on the paid `starter` plan, silently wiping all
production data. Don't rely on Render's disk for anything you can't afford
to lose again.

`render.yaml` still provisions a small disk mounted at `backend/data`, but
it now only backs the local Chroma vector store — a regenerable cache of
resource text (see "Simplifications" above), not source-of-truth data. If
that disk doesn't persist, the fix is a coach re-clicking "Generate concept
explanations," not data recovery. The disk still requires Render's
`starter` plan; if you drop the `disk:` block and use the free plan, Chroma
just rebuilds itself as needed instead of caching between deploys.

**Updating the deployment:** push to `main` — Render auto-deploys on every
push to the branch the Blueprint was created from.
