from pydantic import BaseModel, ValidationError, validator

class FlatsItem(BaseModel):
    project: str
    id: int
    type: str
    price: str
    rooms: str
    area: str
    availability: str

    # just some simple validation example for starters
    @validator('type')
    def type_allowed(cls, v):
        if v not in ['flat','house', 'non-residential']:
            raise ValueError(f"wrong item type: {v}")