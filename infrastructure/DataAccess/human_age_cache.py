from application.Contract.DataAccess.cache_interface import ICache
from application.Contract.DataAccess.human_age_cache_interface import IHumanAgeCache
from domain.Responses.human_age_api_response import HumanAgeApiResponse
from infrastructure.DataAccess.cache import Cache


class HumanAgeCache(IHumanAgeCache):
    def __init__ (self, cache: ICache):
        self.__cache = cache

    async def get_age_for_name(self, name: str) -> HumanAgeApiResponse | None:
        saved_age_for_name = await self.__cache.get_item(name)
        if saved_age_for_name is not None:
            return HumanAgeApiResponse(**saved_age_for_name)
        
    async def save_age_for_name(self, age_for_name: HumanAgeApiResponse) -> None:
        print(f"saving {vars(age_for_name)}")
        await self.__cache.set_item(age_for_name.name, age_for_name)
        
    