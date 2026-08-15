from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.connection import get_db
from app.database.models.document import Document
from app.database.models.workspace import Workspace
from app.database.models.user import User
from app.database.schemas.document import DocumentResponse


router = APIRouter(
    prefix="/workspaces/{workspace_id}/documents",
    tags=["Documents"]
)

# Get all documents of user
@router.get(
    "",
    response_model=list[DocumentResponse]
)
def list_documents(
    workspace_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspace = (
        db.query(Workspace)
        .filter(
            Workspace.id == workspace_id,
            Workspace.user_id == current_user.id
        )
        .first()
    )

    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )

    documents = (
        db.query(Document)
        .filter(Document.workspace_id == workspace_id)
        .all()
    )

    return documents

# Get a single document
@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def get_document(
    workspace_id: int,
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspace = (
        db.query(Workspace)
        .filter(
            Workspace.id == workspace_id,
            Workspace.user_id == current_user.id
        )
        .first()
    )

    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.workspace_id == workspace_id
        )
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    return document

# Delete document
@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_document(
    workspace_id: int,
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    workspace = (
        db.query(Workspace)
        .filter(
            Workspace.id == workspace_id,
            Workspace.user_id == current_user.id
        )
        .first()
    )

    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace not found"
        )

    document = (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.workspace_id == workspace_id
        )
        .first()
    )

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    db.delete(document)
    db.commit()