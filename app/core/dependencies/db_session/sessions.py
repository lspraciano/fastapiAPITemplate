from fastapi import HTTPException
from sqlalchemy.exc import OperationalError, ArgumentError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core.database.database import get_engine_and_session_maker


async def get_db_session() -> AsyncSession:
    try:
        session: async_sessionmaker[AsyncSession]
        _, session = get_engine_and_session_maker()

        async with session() as session:
            yield session
    except (OperationalError, ArgumentError) as error:
        raise HTTPException(
            status_code=503,
            detail=f"database connection error. {error}",
        )
