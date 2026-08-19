from cryptography.fernet import Fernet, InvalidToken

from app.config import settings


def is_configured() -> bool:
    return bool(settings.credential_encryption_key)


def _fernet() -> Fernet:
    return Fernet(settings.credential_encryption_key.encode())


def encrypt(plaintext: str) -> str:
    return _fernet().encrypt(plaintext.encode()).decode()


def decrypt(ciphertext: str) -> str:
    try:
        return _fernet().decrypt(ciphertext.encode()).decode()
    except InvalidToken as e:
        raise ValueError("Stored credential could not be decrypted -- CREDENTIAL_ENCRYPTION_KEY may have changed.") from e
