from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.database.models.user import User
from app.database.schemas.user import UserCreate, UserResponse
from app.auth.hashing import hash_password


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Check if this email is already registered.
    # We do this BEFORE hashing or inserting anything.
    # Without this check, PostgreSQL would raise an IntegrityError
    # (because email has unique=True), which FastAPI would return
    # as an ugly 500 instead of a clean 409.
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An account with this email already exists."
        )

    # Convert plain password into a bcrypt hash.
    # The hash is what gets stored — never the raw password.
    hashed_password = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        profile_image=user.profile_image
    )

    db.add(new_user)
    db.commit()

    # refresh() re-reads the row from PostgreSQL so that
    # auto-generated fields (id, created_at) are populated
    # on the new_user object before we return it.
    db.refresh(new_user)

    return new_user