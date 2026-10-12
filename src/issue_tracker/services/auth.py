from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from issue_tracker.models.users import User
from issue_tracker.repositories.users import create_user, get_user_by_email
from issue_tracker.schemas.users import UserCreate
from issue_tracker.utils.password import hash_password


def register(
    db: Session,
    user_data: UserCreate,
) -> User:
    existing_user = get_user_by_email(db, user_data.email.lower())

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    user = User(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email.lower(),
        photo=user_data.photo,
        password=hash_password(user_data.password),
    )
    return create_user(db, user)