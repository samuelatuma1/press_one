from pydantic import BaseModel

class HumanAgeApiResponse(BaseModel):
    name: str
    age: int | None