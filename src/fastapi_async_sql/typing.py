"""This module defines custom types for the FastAPI Async SQL package."""

from datetime import datetime, timezone

import sqlalchemy as sa


class TimeStamp(sa.types.TypeDecorator):
    impl = sa.types.DateTime
    LOCAL_TIMEZONE = timezone.utc

    def process_bind_param(self, value: datetime | None, dialect):
        """Convert datetime to UTC timezone."""
        if value is None:
            return None
        if value.tzinfo is None:
            value = value.astimezone(self.LOCAL_TIMEZONE)

        return value.astimezone(timezone.utc)

    def process_result_value(self, value, dialect):
        """Convert datetime to UTC timezone."""
        if value is None:
            return None
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)

        return value.astimezone(timezone.utc)
