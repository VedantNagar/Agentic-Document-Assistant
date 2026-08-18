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

    STORAGE_BACKEND: str = "local"
    STORAGE_PATH: str = "storage"

    S3_ENDPOINT_URL: str | None = None
    S3_ACCESS_KEY: str | None = None
    S3_SECRET_KEY: str | None = None
    S3_BUCKET_NAME: str | None = None
    S3_REGION: str | None = None

    MAX_DOCUMENT_SIZE_MB: int = 50
    class Config:
        env_file = ".env"

settings = Settings()