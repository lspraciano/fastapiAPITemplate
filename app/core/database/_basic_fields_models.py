from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr
from sqlalchemy.sql import func


@declarative_mixin
class CommonFields:
    @declared_attr
    def last_change(cls):
        return Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
