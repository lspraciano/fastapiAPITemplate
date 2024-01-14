from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from app.core.database._basic_fields_models import CommonFields
from configuration.configs import settings

db_user: str = settings.get("POSTGRES_USER")
db_password: str = settings.get("POSTGRES_PASSWORD")
db_host: str = settings.get("DATABASE_HOST")
db_port: str = settings.get("DATABASE_PORT")
db_name: str = settings.get("POSTGRES_DB")
database_connection_string: str = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine_async: AsyncEngine = create_async_engine(
    url=database_connection_string,
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
