from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import Depends, FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from pydantic import BaseModel
from redis import asyncio as aioredis
from sqladmin import Admin, ModelView

from app.admin.views import UserAdmin
from app.config import settings
from app.coords.router import router as router_coords
from app.database import engine
from app.images.router import router as router_images
from app.registration.models import Users
from app.registration.router import router as router_registration

from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield

app.router.lifespan_context = lifespan

app.include_router(router_registration)
app.include_router(router_coords)
app.include_router(router_images)

admin = Admin(app, engine)

admin.add_view(UserAdmin)

instrumentator = Instrumentator(
    should_group_status_codes=False,
    excluded_handlers=[".*admin.*", "/metrics"],
)

instrumentator.instrument(app).expose(app)