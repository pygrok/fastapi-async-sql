from fastapi_async_sql.models import BaseSQLModel, BaseTimestampModel, BaseUUIDModel


class Item(BaseSQLModel, BaseTimestampModel, BaseUUIDModel, table=True):
    name: str
