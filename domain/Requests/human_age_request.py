
from pydantic import BaseModel, Field

class HumanAgeRequest(BaseModel):
    name: str = Field(...)