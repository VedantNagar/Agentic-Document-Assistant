from pathlib import Path

from .base import StorageService


class LocalStorage(StorageService):

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(
            parents=True,
            exist_ok=True
        )

    def save(self, file, storage_key: str) -> None:
        file_path = self._get_path(storage_key)

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with file_path.open("wb") as destination:
            while chunk := file.read(1024 * 1024):
                destination.write(chunk)

    def delete(self, storage_key: str) -> None:
        file_path = self._get_path(storage_key)

        if file_path.exists():
            file_path.unlink()

    def exists(self, storage_key: str) -> bool:
        return self._get_path(storage_key).exists()

    def _get_path(self, storage_key: str) -> Path:
        base_path = self.base_path.resolve()
        file_path = (base_path / storage_key).resolve()

        if base_path not in file_path.parents:
            raise ValueError("Invalid storage key")

        return file_path