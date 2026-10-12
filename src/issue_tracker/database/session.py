
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from issue_tracker.database.base import get_db

DbSession = Annotated[Session, Depends(get_db)]