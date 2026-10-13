import uuid

from fastapi import APIRouter, Depends, HTTPException

from issue_tracker.api.deps import get_current_user
from issue_tracker.database.session import DbSession
from issue_tracker.schemas.users import UserResponse
from issue_tracker.services.users import get_user_by_id, get_users

router = APIRouter(dependencies=[Depends(get_current_user)])


@router.get("/", response_model=UserResponse)
def list_users(db: DbSession, page: int = 1, limit: int = 10):
    try:
        users = get_users(db, page=page, limit=limit)
        return UserResponse(message="List of users", data=users)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: uuid.UUID, db: DbSession):
    try:
        user = get_user_by_id(db, user_id)
        return UserResponse(message="User found", data=user)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
