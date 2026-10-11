
issueData: list[dict] = [
    {"id": "12345678-1234-1234-1234-123456789012", "title": "Sample Issue", "description": "This is a sample issue", "status": "open", "priority": "medium"},
    {"id": "12345678-1234-1234-1234-123456789013", "title": "Another Issue", "description": "This is another issue", "status": "in_progress", "priority": "high"},
    {"id": "12345678-1234-1234-1234-123456789014", "title": "Third Issue", "description": "This is the third issue", "status": "closed", "priority": "low"}
]

def get_all_issues() -> list[dict]:
    return issueData

def get_issue_by_id(issue_id: str) -> dict | None:
    for issue in issueData:
        if issue["id"] == issue_id:
            return issue
    return None