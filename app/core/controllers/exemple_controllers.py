from sqlalchemy.future import select

from app.core.database.database import async_session
from app.core.models.exemple_model import ExempleModel


async def create_exemple(
        name: str,
        email: str
) -> ExempleModel:
    new_exemple: ExempleModel = ExempleModel(
        name=name,
        email=email
    )

    async with async_session() as session:
        session.add(new_exemple)
        await session.commit()
        return new_exemple


async def get_all_exemples() -> list[ExempleModel] | None:
    async with async_session() as session:
        query = select(ExempleModel)
        result = await session.execute(query)
        exemples: list[ExempleModel] = result.scalars().unique().all()
    return exemples


async def get_exemple_by_id(
        exemple_id: int
) -> ExempleModel | None:
    async with async_session() as session:
        query = select(ExempleModel).filter(
            ExempleModel.id == exemple_id
        )
        result = await session.execute(query)
        exemple: ExempleModel = result.scalars().unique().one_or_none()

    return exemple
