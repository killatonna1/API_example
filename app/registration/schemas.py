
from pydantic import BaseModel, EmailStr
        
class SUsers(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True