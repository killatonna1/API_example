from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings

if settings.MODE == "TEST":
    DB_URL = settings.TEST_DB_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = settings.DB_URL
    DATABASE_PARAMS = {}

engine = create_async_engine(DB_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

