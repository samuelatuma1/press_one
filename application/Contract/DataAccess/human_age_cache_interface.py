from abc import ABC, abstractmethod

from domain.Responses.human_age_api_response import HumanAgeApiResponse


class IHumanAgeCache(ABC):

    @abstractmethod
    async def get_age_for_name(self, name: str) -> HumanAgeApiResponse | None:
        pass

    @abstractmethod
    async def save_age_for_name(self, age_for_name: HumanAgeApiResponse) -> None:
        pass