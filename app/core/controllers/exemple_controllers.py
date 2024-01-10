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


async def delete_exemplo_by_id(
        exemple_id: int
) -> ExempleModel | None:
    exemple_to_delete: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id
    )

    if not exemple_to_delete:
        return None

    async with async_session() as session:
        await session.delete(exemple_to_delete)
        await session.commit()
        return exemple_to_delete


async def update_exemplo_by_id(
        exemple_id: int,
        name: str | None,
        email: str | None
):
    exemple_to_update: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id
    )

    if not exemple_to_update:
        return None

    if name is not None:
        exemple_to_update.name = name

    if email is not None:
        exemple_to_update.email = email

    async with async_session() as session:
        session.delete(exemple_to_update)
        await session.commit()
        return exemple_to_update
