import uuid
from enum import Enum

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from issue_tracker.models.issues import Issue
from issue_tracker.models.users import User
from issue_tracker.repositories.issues import (
    create_issue as repository_create_issue,
    get_issue_by_id as repository_get_issue_by_id,
    get_issues as repository_get_issues,
    update_issue as repository_update_issue,
)
from issue_tracker.schemas.issues import IssueCreate, IssuePriority, IssueStatus, IssueUpdate


def create_issue(
    db: Session,
    issue_data: IssueCreate,
    current_user: User,
) -> Issue:
    issue = Issue(
        title=issue_data.title,
        description=issue_data.description or "",
        status=IssueStatus.OPEN.value,
        priority=issue_data.priority.value or IssuePriority.MEDIUM.value,
        user_id=current_user.id,
    )
    return repository_create_issue(db, issue)


def get_issue_by_id(
    db: Session,
    issue_id: uuid.UUID,
) -> Issue:
    issue = repository_get_issue_by_id(db, issue_id)

    if issue:
        return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found",
    )


def get_issues(
    db: Session,
    page: int,
    limit: int,
) -> list[Issue]:
    return repository_get_issues(db, page, limit)


def update_issue(
    db: Session,
    issue_id: uuid.UUID,
    issue_data: IssueUpdate,
    current_user: User,
) -> Issue:
    issue = get_issue_by_id(db, issue_id)

    if issue.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not allowed to update this issue",
        )

    updates = issue_data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        if isinstance(value, Enum):
            value = value.value
        setattr(issue, field, value)

    return repository_update_issue(db, issue)
