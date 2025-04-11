"""Repository for Item model."""

from fastapi_async_sql.repositories import BaseRepository

from ..models.item_model import Item
from ..schemas.item_schemas import ItemCreateSchema, ItemUpdateSchema


class ItemRepository(BaseRepository[Item, ItemCreateSchema, ItemUpdateSchema]):
    pass
