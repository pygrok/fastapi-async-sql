from fastapi_async_sql.models import BaseSQLModel, BaseUUIDModel


class Item(BaseSQLModel, BaseUUIDModel, table=True):
    name: str
