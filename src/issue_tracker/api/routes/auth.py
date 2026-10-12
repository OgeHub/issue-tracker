from fastapi import APIRouter, HTTPException, status

from issue_tracker.database.session import DbSession
from issue_tracker.schemas.users import (
    UserCreate,
    UserResponse,
)
from issue_tracker.services.auth import register

router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    db: DbSession,
    user_data: UserCreate,
):
    try:
        user = register(db, user_data)
        return UserResponse(message="User registered successfully", data=user)
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)