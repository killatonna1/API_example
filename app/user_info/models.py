from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
from app.registration.models import *

# class UserInfo(Base):
#     __tablename__ = "User_info"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=True)
#     city = Column(String, nullable=True)
#     birth_date = Column(String, nullable=True)
    
#     user_id = Column(Integer, ForeignKey("Users.id"))
    
#     user_info = relationship("Users", back_populates="users")
    
class UserInfo(Base):
    __tablename__ = "User_info"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    city = Column(String, nullable=True)
    birth_date = Column(String, nullable=True)
    
    iser_id = Column(Integer, ForeignKey("Users.id"))
    
    users = relationship("Users", back_populates="user_info")