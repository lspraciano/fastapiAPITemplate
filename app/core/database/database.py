from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from app.core.database._basic_fields_models import CommonFields
from configuration.configs import settings


engine_async: AsyncEngine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=False
)

async_session = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine_async
)

ModelBase = declarative_base(
    cls=CommonFields
)
