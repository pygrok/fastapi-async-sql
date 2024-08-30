from sqlmodel import Field

from fastapi_async_sql.models import BaseSQLModel


class Item(BaseSQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
