from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from application.Contract.Features.human_age_feature_interface import IHumanAgeFeature
from domain.Requests.human_age_request import HumanAgeRequest


human_age_route = APIRouter()

@human_age_route.post("/", status_code=201)
async def get_human_age(human_age_request: HumanAgeRequest, human_age_feature: IHumanAgeFeature = Depends(IHumanAgeFeature)):
    try:
        return await human_age_feature.get_human_age(human_age_request.name)
    except Exception as ex:
        return JSONResponse(
            status_code=400,
            content={"detail": f"{ex}"},
            headers={"Content-Type": "application/json"},
        )
