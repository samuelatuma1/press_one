
from abc import ABC, abstractmethod

from domain.Responses.human_age_response import HumanAgeResponse


class IHumanAgeFeature(ABC):
    @abstractmethod
    def get_human_age(self, name: str) -> HumanAgeResponse:
        pass