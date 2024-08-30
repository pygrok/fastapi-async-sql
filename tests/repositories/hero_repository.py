"""Repository for Hero model."""

from fastapi_async_sql.repositories import BaseRepository

from ..models.hero_model import Hero
from ..schemas.hero_schemas import HeroCreateSchema, HeroUpdateSchema


class HeroRepository(BaseRepository[Hero, HeroCreateSchema, HeroUpdateSchema]):
    pass
