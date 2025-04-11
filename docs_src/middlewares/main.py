from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine

from fastapi_async_sql.middlewares import AsyncSQLModelMiddleware

app = FastAPI()

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Option 1: Using database URL
app.add_middleware(AsyncSQLModelMiddleware, db_url=DATABASE_URL)

# Option 2: Using custom engine
engine = create_async_engine(DATABASE_URL)
app.add_middleware(AsyncSQLModelMiddleware, custom_engine=engine)
