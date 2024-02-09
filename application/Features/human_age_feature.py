from application.Common.Exceptions.age_not_found_exception import AgeNotFoundException
from application.Common.Utilities.date_time_utility import DateTimeUtility
from application.Contract.Api.age_api_interface import IAgeApi
from application.Contract.DataAccess.human_age_cache_interface import IHumanAgeCache
from application.Contract.Features.human_age_feature_interface import IHumanAgeFeature
from domain.Responses.human_age_api_response import HumanAgeApiResponse
from domain.Responses.human_age_response import HumanAgeResponse


class HumanAgeFeature(IHumanAgeFeature):
    def __init__(self, human_age_cache: IHumanAgeCache, age_api: IAgeApi):
        self.__human_age_cache = human_age_cache
        self.__age_api = age_api

    async def get_human_age(self, name: str) -> HumanAgeResponse:
        cached_age: HumanAgeApiResponse | None = await self.__human_age_cache.get_age_for_name(name)
        
        if cached_age:
            print("Age found in cache:", cached_age)
            return HumanAgeResponse(name=cached_age.name, age=cached_age.age, date_of_birth=DateTimeUtility.get_date_of_birth_from_age(cached_age.age))
        
        print("Age not found in cache, fetching from API...")
        human_age: HumanAgeApiResponse | None = await self.__age_api.get_age_by_name(name)
        
        if not human_age:
            raise AgeNotFoundException(f"Age not found for name {name}")
        
        print("Age fetched from API:", human_age)
        await self.__human_age_cache.save_age_for_name(human_age) # No need to await saving in cache 
        
        return HumanAgeResponse(name=human_age.name, age=human_age.age, date_of_birth=DateTimeUtility.get_date_of_birth_from_age(human_age.age))