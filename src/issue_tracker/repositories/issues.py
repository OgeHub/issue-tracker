import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from issue_tracker.models import Issue


def create_issue(db: Session, issue: Issue) -> Issue:
    db.add(issue)
    db.commit()
    db.refresh(issue)

    return issue


def get_issue_by_id(
    db: Session,
    issue_id: uuid.UUID,
) -> Issue | None:
    return db.get(Issue, issue_id)


def get_issues(
    db: Session,
    page: int = 1,
    limit: int = 10,
) -> list[Issue]:
    offset = (page - 1) * limit

    statement = select(Issue).offset(offset).limit(limit)
    return list(db.scalars(statement).all())


def update_issue(db: Session, issue: Issue) -> Issue:
    db.commit()
    db.refresh(issue)

    return issue
