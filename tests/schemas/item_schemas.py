"""Schemas for Item model."""

from pydantic import UUID4

from fastapi_async_sql.utils.partial import optional

from ..models.item_model import ItemBase


class ItemCreateSchema(ItemBase): ...


@optional()
class ItemUpdateSchema(ItemBase): ...


class ItemReadSchema(ItemBase):
    id: UUID4
    created_by_id: UUID4
