from fastapi import HTTPException, APIRouter,  status
from issue_tracker.schemas.issues import  IssueResponse
from issue_tracker.services.issues import get_all_issues, get_issue_by_id

router = APIRouter()

@router.get("/", response_model=IssueResponse, status_code=status.HTTP_200_OK)
def get_issues():
    issues = get_all_issues()
    return {"message": "List of issues", "data": issues}

@router.get("/{issue_id}", response_model=IssueResponse, status_code=status.HTTP_200_OK)
def get_issue(issue_id: str):
    issue = get_issue_by_id(issue_id)
    if issue:
        return {"message": "Issue found", "data": issue}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found") 

