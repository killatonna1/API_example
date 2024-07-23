from app.dao.base import BaseDao
from app.coords.models import Coords

class CoordsDao(BaseDao):
    model = Coords
    