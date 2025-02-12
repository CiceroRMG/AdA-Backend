from pydantic import BaseModel
from typing import List

class AccommodationSchema(BaseModel):
    id: int
    name: str
    image: List[str] | None = None
    night_price: float
    location: str

    model_config = {
        "from_attributes": True
    }