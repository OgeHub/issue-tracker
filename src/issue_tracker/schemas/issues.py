from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Union
from enum import Enum
from uuid import UUID

class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"
    
class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
    
class IssueCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100, description="The title of the issue")
    description: Optional[str] = Field(None, min_length=1, description="A detailed description of the issue")
    priority: IssuePriority = Field(IssuePriority.MEDIUM, description="The priority of the issue")

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="The title of the issue")
    description: Optional[str] = Field(None, min_length=1, description="A detailed description of the issue")
    status: Optional[IssueStatus] = Field(None, description="The current status of the issue")
    priority: Optional[IssuePriority] = Field(None, description="The priority of the issue")
 
class IssueOut(BaseModel):
    id: UUID
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority

class IssueResponse(BaseModel):
    model_config: ConfigDict = ConfigDict(
        from_attributes=True
    )
    message: str
    data: Optional[Union[IssueOut, list[IssueOut]]] = None