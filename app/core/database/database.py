from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base, DeclarativeMeta

from app.core.database._basic_fields_models import CommonFields
from configuration.configs import settings


def get_engine_and_session_maker() -> tuple[
    AsyncEngine, async_sessionmaker[AsyncSession]
]:
    engine_async: AsyncEngine = create_async_engine(
        url=settings.DB_URI,
        echo=False
    )

    return engine_async, async_sessionmaker(
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
        class_=AsyncSession,
        bind=engine_async
    )


def get_declarative_base() -> DeclarativeMeta:
    metadata: MetaData = MetaData()

    if settings.DB_SCHEMA:
        metadata.schema = settings.DB_SCHEMA

    return declarative_base(
        cls=CommonFields,
        metadata=metadata
    )


ModelBase: DeclarativeMeta = get_declarative_base()
