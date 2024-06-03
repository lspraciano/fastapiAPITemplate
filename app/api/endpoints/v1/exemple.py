from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.controllers.exemple_controllers import create_exemple, get_all_exemples, get_exemple_by_id, \
    delete_exemplo_by_id, update_exemplo_by_id
from app.core.dependencies.db_session.sessions import get_db_session
from app.core.models.exemple_model import ExempleModel
from app.core.schemas.exemple_schema import ExempleSchema, ExempleSchemaCreate, ExempleSchemaUpdate
from app.core.schemas.generic_responses_schemas import generic_response_400

router = APIRouter(
    tags=["Exemple"],
    prefix="/exemple"
)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=ExempleSchema,
    responses=generic_response_400
)
async def create_exemple_(
        new_exemple: ExempleSchemaCreate,
        async_session: AsyncSession = Depends(get_db_session)
):
    new_exemple: ExempleModel = await create_exemple(
        name=new_exemple.name,
        email=new_exemple.email,
        async_session=async_session
    )

    return new_exemple


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=list[ExempleSchema] | None

)
async def get_all_exemples_(
        async_session: AsyncSession = Depends(get_db_session)
):
    all_exemples: list[ExempleModel] | None = await get_all_exemples(
        async_session=async_session
    )

    if not all_exemples:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )

    return all_exemples


@router.get(
    path="/{exemple_id}",
    status_code=status.HTTP_200_OK,
    response_model=ExempleSchema | None
)
async def get_exemples_by_id_(
        exemple_id: int,
        async_session: AsyncSession = Depends(get_db_session)
):
    exemple: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id,
        async_session=async_session
    )

    if not exemple:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )

    return exemple


@router.delete(
    path="/{exemple_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
)
async def delete_exemple_by_id_(
        exemple_id: int,
        async_session: AsyncSession = Depends(get_db_session)
):
    exemple_to_delete: ExempleModel | None = await delete_exemplo_by_id(
        exemple_id=exemple_id,
        async_session=async_session
    )

    if not exemple_to_delete:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )


@router.patch(
    path="/{exemple_id}",
    status_code=status.HTTP_200_OK,
    response_model=ExempleSchema,
    responses=generic_response_400
)
async def update_exemple_by_id_(
        exemple_id: int,
        update_schema: ExempleSchemaUpdate,
        async_session: AsyncSession = Depends(get_db_session)
):
    exemple_to_update: ExempleModel | None = await update_exemplo_by_id(
        exemple_id=exemple_id,
        update_schema=update_schema,
        async_session=async_session
    )

    if not exemple_to_update:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )

    return exemple_to_update
