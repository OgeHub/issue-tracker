import uuid

from fastapi import APIRouter, Depends, HTTPException, status

from issue_tracker.api.deps import CurrentUser, get_current_user
from issue_tracker.database.session import DbSession
from issue_tracker.schemas.issues import IssueCreate, IssueResponse, IssueUpdate
from issue_tracker.services.issues import (
    create_issue,
    get_issue_by_id,
    get_issues,
    update_issue,
)

router = APIRouter(dependencies=[Depends(get_current_user)])

@router.post("/", response_model=IssueResponse, status_code=status.HTTP_201_CREATED)
def create_new_issue(
    db: DbSession,
    current_user: CurrentUser,
    issue_data: IssueCreate,
):
    try:
        issue = create_issue(db, issue_data, current_user)
        return IssueResponse(message="Issue created successfully", data=issue)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/", response_model=IssueResponse)
def list_issues(db: DbSession, page: int = 1, limit: int = 10):
    try:
        issues = get_issues(db, page=page, limit=limit)
        return IssueResponse(message="List of issues", data=issues)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(issue_id: uuid.UUID, db: DbSession):
    try:
        issue = get_issue_by_id(db, issue_id)
        return IssueResponse(message="Issue found", data=issue)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.patch("/{issue_id}", response_model=IssueResponse)
def patch_issue(
    issue_id: uuid.UUID,
    db: DbSession,
    current_user: CurrentUser,
    issue_data: IssueUpdate,
):
    try:
        issue = update_issue(db, issue_id, issue_data, current_user)
        return IssueResponse(message="Issue updated successfully", data=issue)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
