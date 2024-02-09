

from abc import ABC, abstractmethod
import json


class ICache(ABC):
    @abstractmethod
    async def set_item(self, key: str, value: object) -> None:
        pass

    @abstractmethod
    async def get_item(self, key: str) -> object | None:
        pass
