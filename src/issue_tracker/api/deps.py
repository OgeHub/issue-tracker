from typing import Annotated
from uuid import UUID

from fastapi import Cookie, Depends, HTTPException, status

from issue_tracker.database.session import DbSession
from issue_tracker.models.users import User
from issue_tracker.repositories.users import get_user_by_id
from issue_tracker.utils.jwt import verify_access_token


def get_current_user(
    db: DbSession,
    access_token: Annotated[str | None, Cookie()] = None,
) -> User:
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        user_id = UUID(verify_access_token(access_token))
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
