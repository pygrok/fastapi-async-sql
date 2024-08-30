from typing import Annotated

from fastapi import Depends, FastAPI, Request
from sqlmodel import Field, SQLModel, select
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi_async_sql.middlewares import AsyncSQLModelMiddleware

app = FastAPI()

# Define the database URL
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Add the middleware to the FastAPI app
app.add_middleware(AsyncSQLModelMiddleware, db_url=DATABASE_URL)


# Example model
class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str


# Dependency that extracts the session from the request state
async def get_session(request: Request) -> AsyncSession:
    return request.state.db


# Annotate the get_session dependency, so you can use it in routes
AsyncSessionDependency = Annotated[AsyncSession, Depends(get_session)]


@app.get("/items")
async def read_items(session: AsyncSessionDependency):
    items = await session.exec(select(Item))
    return items
