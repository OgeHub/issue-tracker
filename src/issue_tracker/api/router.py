from fastapi import APIRouter
from src.issue_tracker.api.routes import issues

router = APIRouter()

router.include_router(issues.router, prefix="/issues", tags=["Issues"])