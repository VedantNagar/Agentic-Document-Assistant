from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    Data required when creating a user.
    """

    name: str

    email: EmailStr

    password: str

    profile_image: str | None = None



class UserResponse(BaseModel):
    """
    Data returned to frontend.
    """

    id: int

    name: str

    email: EmailStr

    profile_image: str | None = None


    class Config:
        from_attributes = True