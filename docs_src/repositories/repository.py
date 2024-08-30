from typing import Annotated

from fastapi import Depends, FastAPI, Request
from pydantic import UUID4

from fastapi_async_sql.middlewares import AsyncSQLModelMiddleware
from fastapi_async_sql.models import BaseSQLModel
from fastapi_async_sql.repositories import BaseRepository
from fastapi_async_sql.utils.partial import optional

app = FastAPI()
app.add_middleware(AsyncSQLModelMiddleware, db_url="sqlite+aiosqlite:///./test.db")


class ItemBase(BaseSQLModel):
    name: str


class Item(ItemBase, table=True): ...


class ItemCreateSchema(ItemBase): ...


@optional()
class ItemUpdateSchema(ItemBase): ...


class ItemReadSchema(ItemBase):
    id: UUID4


class ItemRepository(BaseRepository[Item, ItemCreateSchema, ItemUpdateSchema]):
    pass


def get_item_repository(request: Request) -> ItemRepository:
    return ItemRepository(Item, request.state.db)


ItemRepositoryDependency = Annotated[ItemRepository, Depends(get_item_repository)]


@app.get("/items/", response_model=list[ItemReadSchema])
async def read_items(
    item_repository: ItemRepositoryDependency,
):
    return await item_repository.get_multi()


@app.post("/items/", response_model=ItemReadSchema)
async def create_item(
    item_repository: ItemRepositoryDependency,
    item_in: ItemCreateSchema,
):
    return await item_repository.create(obj_in=item_in)


@app.patch("/items/{item_id}", response_model=ItemReadSchema)
async def update_item(
    item_repository: ItemRepositoryDependency,
    item_id: UUID4,
    item_new: ItemUpdateSchema,
):
    item_current = await item_repository.get(id=item_id)
    return await item_repository.update(obj_current=item_current, obj_new=item_new)


@app.delete("/items/{item_id}")
async def delete_item(
    item_repository: ItemRepositoryDependency,
    item_id: UUID4,
):
    item = await item_repository.get(id=item_id)
    await item_repository.remove(id=item.id)
    return None
