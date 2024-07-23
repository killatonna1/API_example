
from fastapi import APIRouter, Depends, HTTPException, Response, status, BackgroundTasks

from app.exceptions import UserAlredyExistsException
from app.registration.dao import UsersDao

from app.user_info.models import UserInfo
from app.user_info.schemas import SUserInfo
from app.user_info.dao import BaseDao

from app.registration.auth import get_password_hash

router = APIRouter(
    prefix="/user_info",
    tags=["user-info"],
)

@router.post("/user_info")
async def add_user_info(
    background_tasks: BackgroundTasks,
    user_data: SUserInfo):
    existing_user =  await UsersDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlredyExistsException
    hashed_password = get_password_hash(user_data.password)
    user = await UsersDao.add_registration(email = user_data.email,
                                   password = hashed_password,
                                   )
