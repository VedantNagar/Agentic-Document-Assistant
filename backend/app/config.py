from pydantic_settings import BaseSettings
class Settings(BaseSettings):

    # PostgreSQL connection string
    DATABASE_URL: str


    # Secret key used for signing JWT tokens
    SECRET_KEY: str


    # JWT algorithm
    ALGORITHM: str = "HS256"


    # Token expiry time in minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 300


    class Config:
        env_file = ".env"

settings = Settings()