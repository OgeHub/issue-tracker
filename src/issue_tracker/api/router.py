from fastapi import APIRouter
from issue_tracker.api.routes import auth
from issue_tracker.api.routes import issues
from issue_tracker.api.routes import users

router = APIRouter()

router.include_router(issues.router, prefix="/issues", tags=["Issues"])
router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(users.router, prefix="/users", tags=["Users"])