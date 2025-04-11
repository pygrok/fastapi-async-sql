from fastapi import FastAPI, Request
from sqlmodel import Field, Relationship

from fastapi_async_sql.middlewares import AsyncSQLModelMiddleware
from fastapi_async_sql.models import BaseSQLModel

app = FastAPI()
app.add_middleware(AsyncSQLModelMiddleware, db_url="sqlite+aiosqlite:///./test.db")


class User(BaseSQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    posts: list["Post"] = Relationship(back_populates="user")


class Post(BaseSQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int = Field(foreign_key="user.id")
    user: "User" = Relationship(back_populates="posts")


# Example of accessing the relationship
@app.get("/users/{user_id}/posts")
async def get_user_posts(request: Request, user_id: int):
    user = await request.state.db.get(User, user_id)

    # Accessing the lazy-loaded relationship with awaitable_attrs
    posts = await user.awaitable_attrs.posts

    return posts
