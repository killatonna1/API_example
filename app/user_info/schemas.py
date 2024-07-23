
from pydantic import BaseModel, EmailStr
from datetime import date
        
class SUserInfo(BaseModel):
    name: str
    city: str
    birth_date: date
    
    class Config:
        orm_mode = True