import asyncio

import json

import pytest

from sqlalchemy import insert

from app.database import Base, async_session_maker, engine
from app.config import settings
from app.registration.models import *
from app.user_info.models import *
from app.coords.models import *
from app.main import app as fastapi_app

from fastapi.testclient import TestClient
from httpx import AsyncClient


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    
    def open_mock_json(model:str):
        with open(f"app/tests/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)
        
    user_info = open_mock_json("user_info")
    registration = open_mock_json("registration")
    
    async with async_session_maker() as session:
        add_registration = insert(UserInfo).values(user_info)
        add_user_info = insert(Users).values(registration)
        
        await session.execute(add_registration)
        await session.execute(add_user_info)
        
        await session.commit()
        
# Из документации pytest-asyncio
@pytest.fixture(scope="session")
def event_loop(request):
    """Create as instance of default event loop for each test case"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
    

@pytest.fixture(scope="function")
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        async with async_session_maker() as session:
            yield session
                