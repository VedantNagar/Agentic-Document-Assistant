import boto3
from botocore.exceptions import ClientError

from .base import StorageService


class S3Storage(StorageService):

    def __init__(
        self,
        endpoint_url: str | None,
        access_key: str,
        secret_key: str,
        bucket_name: str,
        region: str | None = None,
    ):
        self.bucket_name = bucket_name

        self.client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )

    def save(self, file, storage_key: str) -> None:
        self.client.upload_fileobj(
            file,
            self.bucket_name,
            storage_key,
        )

    def delete(self, storage_key: str) -> None:
        self.client.delete_object(
            Bucket=self.bucket_name,
            Key=storage_key,
        )

    def exists(self, storage_key: str) -> bool:
        try:
            self.client.head_object(
                Bucket=self.bucket_name,
                Key=storage_key,
            )
            return True

        except ClientError as error:
            error_code = error.response.get("Error", {}).get("Code")

            if error_code in ("404", "NoSuchKey", "NotFound"):
                return False

            raise