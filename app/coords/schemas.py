
from pydantic import BaseModel, EmailStr

class SCoords(BaseModel):
    id: int
    app_generated_id: str
    coordinates: list[float]
    
    
    class Config:
        orm_mode = True