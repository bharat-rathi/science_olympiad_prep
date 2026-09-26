"""Student login credentials -- stdlib-only, no bcrypt/passlib dependency.

Coaches authenticate via Google OAuth (see auth.py); students don't have
Google accounts to rely on, so they get a coach-issued PIN instead. Kept to
the standard library since adding a new pip dependency means another deploy
to get it through -- pbkdf2_hmac is slow enough per-guess to be a reasonable
choice for a short PIN, given the account has no other attack surface
(no email, no username enumeration value beyond a name).
"""

import hashlib
import hmac
import secrets

_ITERATIONS = 390_000
# Avoids visually ambiguous characters (0/O, 1/I/L) since this is read off a
# screen by a coach and typed by a student, not copy-pasted.
_PIN_ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789"


def generate_pin(length: int = 6) -> str:
    return "".join(secrets.choice(_PIN_ALPHABET) for _ in range(length))


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), _ITERATIONS).hex()
    return f"{salt}${digest}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt, digest = stored.split("$", 1)
    except ValueError:
        return False
    candidate = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), _ITERATIONS).hex()
    return hmac.compare_digest(candidate, digest)
