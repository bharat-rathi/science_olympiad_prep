from fastapi import APIRouter, Depends, HTTPException, Request, Response
from sqlalchemy.orm import Session

from app import auth, models, schemas
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


@router.post("/register", response_model=schemas.CoachOut)
def register(payload: schemas.RegisterRequest, request: Request, response: Response, db: Session = Depends(get_db)):
    is_bootstrap = db.query(models.Coach).count() == 0
    if not is_bootstrap and request.state.coach is None:
        raise HTTPException(403, "Log in first to add a teammate's account")

    if db.query(models.Coach).filter(models.Coach.name == payload.name).first():
        raise HTTPException(409, "That name is already taken")
    if len(payload.password) < 8:
        raise HTTPException(400, "Password must be at least 8 characters")

    coach = models.Coach(name=payload.name, password_hash=auth.hash_password(payload.password))
    db.add(coach)
    db.commit()
    db.refresh(coach)

    if is_bootstrap:
        token = auth.create_session(db, coach)
        _set_session_cookie(response, request, token)

    return coach


@router.post("/login", response_model=schemas.CoachOut)
def login(payload: schemas.LoginRequest, request: Request, response: Response, db: Session = Depends(get_db)):
    coach = db.query(models.Coach).filter(models.Coach.name == payload.name).first()
    if not coach or not auth.verify_password(payload.password, coach.password_hash):
        raise HTTPException(401, "Incorrect name or password")

    token = auth.create_session(db, coach)
    _set_session_cookie(response, request, token)
    return coach


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
