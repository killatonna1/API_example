from sqlalchemy import select, insert
from app.database import async_session_maker


class BaseDao:
    model = None
    
    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()
    
    @classmethod
    async def get_all_rows(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_one_or_none(cls, **kwargs):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**kwargs)
            result = await session.execute(query)
            return result.scalars().one_or_none()
        
    @classmethod
    async def add_data(cls, **kwargs):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**kwargs)
            await session.execute(query)
            await session.commit()
            
        