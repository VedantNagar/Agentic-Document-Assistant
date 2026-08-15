from datetime import datetime

from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    workspace_id: int
    filename: str
    mime_type: str
    file_size: int
    storage_key: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True