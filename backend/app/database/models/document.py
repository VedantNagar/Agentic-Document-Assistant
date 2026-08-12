from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..connection import Base


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    workspace_id = Column(
        Integer,
        ForeignKey("workspaces.id"),
        nullable=False
    )

    filename = Column(
        String,
        nullable=False
    )

    mime_type = Column(
        String,
        nullable=False
    )

    file_size = Column(
        Integer,
        nullable=False
    )

    storage_key = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="uploaded"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    workspace = relationship(
        "Workspace",
        back_populates="documents"
    )