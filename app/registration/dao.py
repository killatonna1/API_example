from app.dao.base import BaseDao
from app.registration.models import Users

from sqlalchemy import insert
from app.database import async_session_maker

class UsersDao(BaseDao):
    model = Users
    

    @classmethod
    async def add_registration(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs).returning(Users)
            await session.execute(query)
            await session.commit()