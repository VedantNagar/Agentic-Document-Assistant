from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..connection import Base
from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = "users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )


    hashed_password = Column(
        String,
        nullable=False
    )

    profile_image = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    workspaces = relationship(
        "Workspace",
        back_populates = "user",
        cascade = "all, delete-orphan"  
        # cascade so that workspaces do not become orphan when user is deleted
    )