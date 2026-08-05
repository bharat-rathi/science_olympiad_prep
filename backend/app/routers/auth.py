from fastapi import APIRouter, Depends, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app import auth, models, schemas
from app.config import settings
from app.db import get_db

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
