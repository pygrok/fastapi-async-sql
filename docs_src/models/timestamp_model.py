from fastapi_async_sql.models import BaseSQLModel, BaseTimestampModel


class Item(BaseSQLModel, BaseTimestampModel, table=True):
    name: str
