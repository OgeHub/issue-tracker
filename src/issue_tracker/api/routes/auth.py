from fastapi import APIRouter, HTTPException, Response, status

from issue_tracker.database.session import DbSession
from issue_tracker.schemas.users import (
    UserCreate,
    UserResponse,
    UserLogin,
    UserLoginResponse,
)
from issue_tracker.services.auth import register, login

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
   
@router.post(
    "/login",
    response_model=UserLoginResponse,
) 
def login_user(
    db: DbSession,
    response: Response,
    payload: UserLogin,
):
    try:
        access_token = login(db, payload)
        
        # set cookie with the access token
        
        response.set_cookie(key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=30 * 60,
        path="/")
        
        return UserLoginResponse(message="Login successful")
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)