from sqlalchemy import Select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.models.exemple_model import ExempleModel
from app.core.schemas.exemple_schema import ExempleSchemaUpdate, ExempleSchemaCreate


async def create_exemple(
        create_schema: ExempleSchemaCreate,
        async_session: AsyncSession,
) -> ExempleModel:
    new_exemple: ExempleModel = ExempleModel(
        **create_schema.model_dump(exclude_unset=True),
    )

    async_session.add(new_exemple)
    await async_session.commit()
    return new_exemple


async def get_all_exemples(
        async_session: AsyncSession,
) -> list[ExempleModel] | None:
    exemples_list: list[ExempleModel] = []
    query: Select = select(ExempleModel)
    scalar_results: ScalarResult = await async_session.scalars(statement=query)

    for scalar_result in scalar_results:
        exemples_list.append(scalar_result)

    return exemples_list


async def get_exemple_by_id(
        exemple_id: int,
        async_session: AsyncSession,
) -> ExempleModel | None:
    query: Select = select(ExempleModel).where(
        exemple_id == ExempleModel.id
    )

    exemple: ExempleModel | None = await async_session.scalar(statement=query)

    return exemple


async def delete_exemplo_by_id(
        exemple_id: int,
        async_session: AsyncSession,
) -> ExempleModel | None:
    exemple_to_delete: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id,
        async_session=async_session
    )

    if not exemple_to_delete:
        return None

    await async_session.delete(instance=exemple_to_delete)
    await async_session.commit()
    return exemple_to_delete


async def update_exemplo_by_id(
        exemple_id: int,
        update_schema: ExempleSchemaUpdate,
        async_session: AsyncSession,
):
    exemple_to_update: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id,
        async_session=async_session
    )

    if not exemple_to_update:
        return None

    for field, value in update_schema.model_dump(exclude_unset=True).items():
        if hasattr(ExempleModel, field):
            setattr(exemple_to_update, field, value)

    async_session.add(instance=exemple_to_update)
    await async_session.commit()
    await async_session.refresh(instance=exemple_to_update)
    return exemple_to_update
