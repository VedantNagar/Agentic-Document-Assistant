from datetime import datetime

from pydantic import BaseModel


class WorkspaceCreate(BaseModel):
    name: str
    description: str | None = None


class WorkspaceUpdate(BaseModel):
    name: str | None = None
    description: str | None = None


class WorkspaceResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True

# Pydantic normally expects something like a dictionary
# from_attributes = True tells Pydantic:
# "You can build this response from the attributes of a SQLAlchemy object."