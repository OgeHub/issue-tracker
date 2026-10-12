import uuid

from fastapi import HTTPException
from sqlalchemy.orm import Session

from issue_tracker.models.users import User
from issue_tracker.repositories.users import (
    get_user_by_id as repository_get_user_by_id,
    get_users as repository_get_users,
)

def get_user_by_id(
    db: Session,
    user_id: uuid.UUID,
) -> User | None:
    user = repository_get_user_by_id(db, user_id)
    
    if user:
        return user
    
    raise HTTPException(status_code=404, detail="User not found")


def get_users(
    db: Session,
    page: int,
    limit: int,
) -> list[User]:
    return repository_get_users(db, page, limit)
