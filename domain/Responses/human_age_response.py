from pydantic import BaseModel, Field

class HumanAgeResponse(BaseModel):
    name: str
    age: int
    date_of_birth: int