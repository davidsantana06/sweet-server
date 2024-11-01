from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin():
    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=datetime.now)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now,
            onupdate=datetime.now
        )
