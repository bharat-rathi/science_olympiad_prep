from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app import auth, crypto, models, schemas
from app.config import settings
from app.db import get_db
from app.llm.router import get_llm_handle

router = APIRouter(prefix="/api/auth", tags=["auth"])


def _set_session_cookie(response: Response, request: Request, token: str) -> None:
    response.set_cookie(
        auth.SESSION_COOKIE_NAME,
        token,
        max_age=auth.SESSION_TTL_DAYS * 24 * 3600,
        httponly=True,
        samesite="lax",
        secure=request.url.scheme == "https",
    )


@router.get("/google/login")
async def google_login(request: Request):
    redirect_uri = f"{settings.public_base_url}/api/auth/google/callback"
    return await auth.oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/drive/connect")
async def google_drive_connect(request: Request, coach: models.Coach = Depends(auth.require_coach)):
    """Separate, opt-in consent flow for Google Drive access -- distinct
    from the plain login above, only triggered when a coach explicitly
    wants to add a Drive video, not bundled into every sign-in.

    access_type=offline + prompt=consent forces Google to return a
    refresh_token (it only does so on first consent otherwise), since a
    coach pastes a Drive link long after this login-time exchange, not
    during it.
    """
    redirect_uri = f"{settings.public_base_url}/api/auth/google/drive/callback"
    return await auth.oauth.google.authorize_redirect(
        request,
        redirect_uri,
        scope="openid email profile https://www.googleapis.com/auth/drive.readonly",
        access_type="offline",
        prompt="consent",
    )


@router.get("/google/drive/callback")
async def google_drive_callback(request: Request, db: Session = Depends(get_db)):
    coach = request.state.coach
    if coach is None:
        return RedirectResponse(f"{settings.public_base_url}/login")

    oauth_token = await auth.oauth.google.authorize_access_token(request)
    refresh_token = oauth_token.get("refresh_token")
    if refresh_token:
        row = db.get(models.Coach, coach.id)
        row.google_drive_refresh_token_encrypted = crypto.encrypt(refresh_token)
        db.commit()
    # No refresh_token in the response means the coach had already granted
    # this scope before and Google didn't re-issue one -- their existing
    # stored token (if any) is left as-is rather than overwritten with None.
    return RedirectResponse(f"{settings.public_base_url}/settings")


@router.post("/drive/disconnect", response_model=schemas.DriveStatusOut)
def drive_disconnect(coach: models.Coach = Depends(auth.require_coach), db: Session = Depends(get_db)):
    row = db.get(models.Coach, coach.id)
    row.google_drive_refresh_token_encrypted = None
    db.commit()
    return schemas.DriveStatusOut(connected=False)


@router.get("/drive-status", response_model=schemas.DriveStatusOut)
def drive_status(coach: models.Coach = Depends(auth.require_coach)):
    return schemas.DriveStatusOut(connected=bool(coach.google_drive_refresh_token_encrypted))


@router.get("/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Finish the OAuth round-trip and turn a Google identity into a Coach.

    A Coach row with email set but google_sub still NULL means "invited but
    hasn't signed in yet" (see /invite below) -- this is where that row gets
    claimed. The very first account ever (nobody invited, nobody exists) is
    allowed to self-create, same bootstrap rule the old password flow had.
    """
    oauth_token = await auth.oauth.google.authorize_access_token(request)
    userinfo = oauth_token["userinfo"]
    email = userinfo["email"]
    name = userinfo.get("name") or email
    google_sub = userinfo["sub"]

    coach = db.query(models.Coach).filter(models.Coach.email == email).first()
    if coach is None:
        is_bootstrap = db.query(models.Coach).count() == 0
        if not is_bootstrap:
            return RedirectResponse(f"{settings.public_base_url}/login?error=not_invited")
        coach = models.Coach(email=email, name=name, google_sub=google_sub)
        db.add(coach)
    else:
        coach.google_sub = google_sub
        coach.name = name
    db.commit()
    db.refresh(coach)

    session_token = auth.create_session(db, coach)
    response = RedirectResponse(f"{settings.public_base_url}/")
    _set_session_cookie(response, request, session_token)
    return response


@router.post("/invite", response_model=schemas.CoachOut)
def invite(payload: schemas.InviteRequest, coach: models.Coach = Depends(auth.require_coach), db: Session = Depends(get_db)):
    email = payload.email.strip().lower()
    if db.query(models.Coach).filter(models.Coach.email == email).first():
        raise HTTPException(409, "That email has already been invited or has an account")

    invited = models.Coach(email=email, invited_by_coach_id=coach.id)
    db.add(invited)
    db.commit()
    db.refresh(invited)
    return invited


@router.post("/logout")
def logout(request: Request, response: Response, db: Session = Depends(get_db)):
    token = request.cookies.get(auth.SESSION_COOKIE_NAME)
    if token:
        auth.delete_session(db, token)
    response.delete_cookie(auth.SESSION_COOKIE_NAME)
    return {"ok": True}


@router.get("/me", response_model=schemas.MeResponse)
def me(request: Request, db: Session = Depends(get_db)):
    coach = request.state.coach
    if coach:
        return schemas.MeResponse(authenticated=True, coach=coach)
    needs_bootstrap = db.query(models.Coach).count() == 0
    return schemas.MeResponse(authenticated=False, needs_bootstrap=needs_bootstrap)


@router.get("/ai-settings", response_model=schemas.AiSettingsOut)
def get_ai_settings(coach: models.Coach = Depends(auth.require_coach)):
    return schemas.AiSettingsOut(provider=coach.llm_provider, has_key=bool(coach.llm_api_key_encrypted))


@router.put("/ai-settings", response_model=schemas.AiSettingsOut)
def update_ai_settings(
    payload: schemas.AiSettingsUpdate,
    coach: models.Coach = Depends(auth.require_coach),
    db: Session = Depends(get_db),
):
    """Save (or clear) a coach's personal LLM provider + key.

    A non-null provider always requires a fresh, working key -- we never
    keep an old key around under a newly-picked provider, and we verify the
    key with one cheap live call before persisting anything, so a typo
    surfaces immediately instead of on the next real generation.

    `coach` (from the auth dependency) was loaded in the middleware's own
    DB session, not this endpoint's -- re-fetch it in `db` before mutating,
    or `db.commit()`/`db.refresh()` raise "not persistent within this
    Session".
    """
    row = db.get(models.Coach, coach.id)

    if payload.provider is None:
        row.llm_provider = None
        row.llm_api_key_encrypted = None
        db.commit()
        return schemas.AiSettingsOut(provider=None, has_key=False)

    if payload.provider not in ("gemini", "claude", "openai"):
        raise HTTPException(400, "Unknown provider.")
    if not payload.api_key or not payload.api_key.strip():
        raise HTTPException(400, "An API key is required to use a personal provider.")
    if not crypto.is_configured():
        raise HTTPException(503, "AI provider settings aren't configured on this server yet.")

    probe = models.Coach(llm_provider=payload.provider, llm_api_key_encrypted=None)
    try:
        get_llm_handle(probe, raw_api_key=payload.api_key.strip()).complete_text(
            "You are a test.", "Say OK.", max_tokens=5, effort="low", label="ai_settings_probe"
        )
    except Exception as e:
        raise HTTPException(400, f"That {payload.provider} API key didn't work -- double check it and try again.") from e

    row.llm_provider = payload.provider
    row.llm_api_key_encrypted = crypto.encrypt(payload.api_key.strip())
    db.commit()
    return schemas.AiSettingsOut(provider=row.llm_provider, has_key=True)
