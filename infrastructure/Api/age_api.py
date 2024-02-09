import json
from application.Contract.Api.age_api_interface import IAgeApi
from domain.Responses.human_age_api_response import HumanAgeApiResponse


from infrastructure.Api.base_api_request import BaseApiRequest



class AgeApi(BaseApiRequest, IAgeApi):

    async def get_age_by_name(self, name: str) -> HumanAgeApiResponse | None:
        request_url = f"https://api.agify.io/?name={name}"
        json_data = await self.get_data(request_url)
        if json_data is not None:
            age_response =  HumanAgeApiResponse(**json_data)
            return None if age_response.age is None else age_response
        
        return None
        
    