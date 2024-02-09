from abc import ABC, abstractmethod

from domain.Responses.human_age_api_response import HumanAgeApiResponse


class IAgeApi(ABC):
    @abstractmethod
    async def get_age_by_name(self, name: str) -> HumanAgeApiResponse | None:
        pass