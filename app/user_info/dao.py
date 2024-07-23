from app.dao.base import BaseDao
from app.user_info.models import UserInfo

from sqlalchemy import insert
from app.database import async_session_maker

class UsersDao(BaseDao):
    model = UserInfo
    

    @classmethod
    async def add_user_info(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs).returning(UserInfo)
            await session.execute(query)
            await session.commit()