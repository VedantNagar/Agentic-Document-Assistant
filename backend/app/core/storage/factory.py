from app.config import settings

from .base import StorageService
from .local import LocalStorage
from .s3 import S3Storage


def get_storage() -> StorageService:

    if settings.STORAGE_BACKEND == "local":
        return LocalStorage(
            base_path=settings.STORAGE_PATH
        )

    if settings.STORAGE_BACKEND == "s3":
        if not all(
            [
                settings.S3_ACCESS_KEY,
                settings.S3_SECRET_KEY,
                settings.S3_BUCKET_NAME,
            ]
        ):
            raise ValueError(
                "S3 storage is enabled but S3 configuration is incomplete"
            )

        return S3Storage(
            endpoint_url=settings.S3_ENDPOINT_URL,
            access_key=settings.S3_ACCESS_KEY,
            secret_key=settings.S3_SECRET_KEY,
            bucket_name=settings.S3_BUCKET_NAME,
            region=settings.S3_REGION,
        )

    raise ValueError(
        f"Unsupported storage backend: {settings.STORAGE_BACKEND}"
    )