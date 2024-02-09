from application.Contract.Api.age_api_interface import IAgeApi
from domain.Responses.human_age_api_response import HumanAgeApiResponse

class FakeAgeApi(IAgeApi):
    async def get_age_by_name(self, name: str) -> HumanAgeApiResponse | None:
        return HumanAgeApiResponse(name = name, age = 2)
    
class FakeAgeApiReturningNoneForGetAgeByName(IAgeApi):
    async def get_age_by_name(self, name: str) -> HumanAgeApiResponse | None:
        return None