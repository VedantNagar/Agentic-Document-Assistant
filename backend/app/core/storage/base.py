from abc import ABC, abstractmethod


class StorageService(ABC):

    @abstractmethod
    def save(self, file, storage_key: str) -> None:
        pass

    @abstractmethod
    def delete(self, storage_key: str) -> None:
        pass

    @abstractmethod
    def exists(self, storage_key: str) -> bool:
        pass