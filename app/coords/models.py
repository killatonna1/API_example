from sqlalchemy import ARRAY, Column, Float, Integer, String
from app.database import Base
   
    
class Coords(Base):
    __tablename__ = "coords_table"
    
    id = Column(Integer, primary_key=True)
    app_generated_id = Column(String, nullable=True)
    coordinates = Column(ARRAY(Float), nullable=True)
    # email = Column(String, nullable=True)
    # password = Column(String, nullable=True)
