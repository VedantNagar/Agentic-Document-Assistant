from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models.user import User
from app.database.models.workspace import Workspace
from app.database.schemas.workspace import (
    WorkspaceCreate,
    WorkspaceResponse
)


router = APIRouter(
    prefix="/workspaces",
    tags=["Workspaces"]
)

# Creating a new workspace
@router.post(
    "",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_201_CREATED
)
def create_workspace(
    workspace: WorkspaceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_workspace = Workspace(
        name=workspace.name,
        description=workspace.description,
        user_id=current_user.id
    )

    db.add(new_workspace)
    db.commit()
    db.refresh(new_workspace)

    return new_workspace

# Getting workspace(s)
@router.get(
    "",
    response_model=list[WorkspaceResponse]
)
def get_workspaces(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspaces = (
        db.query(Workspace)
        .filter(Workspace.user_id == current_user.id)
        .all()
    )

    return workspaces