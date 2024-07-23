from sqlalchemy import ARRAY, Column, Float, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship
from app.user_info.models import *
    
# class Users(Base):
#     __tablename__ = "Users"
    
#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     password = Column(String, nullable=False)
    
#     users = relationship("UserInfo", back_populates="user_info")
    
class Users(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    user_info = relationship("UserInfo", back_populates="users")