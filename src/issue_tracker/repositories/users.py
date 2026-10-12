import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from issue_tracker.models import User


def create_user(db: Session, user: User) -> User:
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_id(
    db: Session,
    user_id: uuid.UUID,
) -> User | None:
    return db.get(User, user_id)


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    statement = select(User).where(User.email == email)
    return db.scalar(statement)


def get_users(
    db: Session,
    page: int = 1,
    limit: int = 10,
) -> list[User]:
    offset = (page - 1) * limit
    
    statement = select(User).offset(offset).limit(limit)
    return list(db.scalars(statement).all())