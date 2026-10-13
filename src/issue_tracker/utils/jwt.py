from datetime import datetime, timedelta, timezone
from uuid import UUID
import jwt

from issue_tracker.utils.settings import settings

SECRET_KEY = settings.jwt_secret_key
ALGORITHM = "HS256"
EXPIRE_MINUTES = settings.jwt_expiration_minutes


def create_access_token(user_id: UUID | str) -> str:
    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=EXPIRE_MINUTES
    )

    payload = {
        "sub": str(user_id),
        "exp": expires_at,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def verify_access_token(token: str) -> str:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        user_id = payload.get("sub")
        if user_id is None:
            raise ValueError("Invalid token")
        return str(user_id)
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")
