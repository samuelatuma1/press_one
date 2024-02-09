from application.Contract.DataAccess.human_age_cache_interface import IHumanAgeCache
from domain.Responses.human_age_api_response import HumanAgeApiResponse


class FakeHumanAgeCache(IHumanAgeCache):
    async def get_age_for_name(self, name: str) -> HumanAgeApiResponse | None:
        return HumanAgeApiResponse(name = name, age = 1)
    
    async def save_age_for_name(self, age_for_name: HumanAgeApiResponse) -> None:
        pass

class FakeHumanAgeCacheReturnsNoneForGetAgeByName(IHumanAgeCache):
    async def get_age_for_name(self, name: str) -> HumanAgeApiResponse | None:
        return None
    
    async def save_age_for_name(self, age_for_name: HumanAgeApiResponse) -> None:
        pass
    
    