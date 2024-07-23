import asyncio
from fastapi import APIRouter, Depends, HTTPException, Request, Response, status

from app.coords.models import Coords
from app.registration.dao import UsersDao
from app.coords.schemas import SCoords
from app.coords.dao import BaseDao, CoordsDao
from app.registration.dependencies import get_current_user
from app.registration.models import Users

from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/get_coords",
    tags=["Координаты"],
)



@router.get("")
@cache(expire=60)
async def get_users(user: Users = Depends(get_current_user)):
    print(user, type(user), user.id)
    coords_data = await CoordsDao.find_one_or_none(id=user.id)
    if coords_data:
        await asyncio.sleep(3)
        return coords_data.coordinates
    else:
        return None
    
# @router.post("")
# async def add_coords(
#     user: Users = Depends(get_current_user),
# ):
#     await CoordsDao.add()