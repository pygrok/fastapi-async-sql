"""Schemas for Hero model."""

from pydantic import UUID4

from fastapi_async_sql.utils.partial import optional

from ..models.hero_model import HeroBase
from ..models.item_model import ItemBase
from ..models.team_model import TeamBase


class HeroCreateSchema(HeroBase):
    pass


@optional()
class HeroUpdateSchema(HeroBase):
    team_id: UUID4 | None = None
    item_id: UUID4 | None = None


class HeroReadSchema(HeroBase):
    id: UUID4


class _HeroTeamReadSchema(TeamBase):
    id: UUID4


class _ItemTeamReadSchema(ItemBase):
    id: UUID4
    created_by_id: UUID4


class HeroReadWithTeamSchema(HeroReadSchema):
    id: UUID4
    team: _HeroTeamReadSchema = None
    item: _ItemTeamReadSchema = None
