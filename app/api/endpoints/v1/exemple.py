from fastapi import APIRouter, status, HTTPException

from app.core.controllers.exemple_controllers import create_exemple, get_all_exemples, get_exemple_by_id
from app.core.models.exemple_model import ExempleModel
from app.core.schemas.exemple_schema import ExempleResponseSchema, ExempleSchemaCreate
from app.core.schemas.generic_responses_schemas import generics_responses

router = APIRouter(
    tags=["Exemple"],
    prefix="/exemple"
)


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=ExempleResponseSchema
)
async def create_exemple_(
        new_exemple: ExempleSchemaCreate
):
    new_exemple: ExempleModel = await create_exemple(
        name=new_exemple.name,
        email=new_exemple.email
    )

    return new_exemple


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=list[ExempleResponseSchema] | None,
    responses=generics_responses

)
async def get_all_exemples_():
    all_exemples: list[ExempleModel] | None = await get_all_exemples()

    if not all_exemples:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )

    return all_exemples


@router.get(
    path="/{exemple_id}",
    status_code=status.HTTP_200_OK,
    response_model=ExempleResponseSchema | None,
    responses=generics_responses
)
async def get_exemples_by_id_(
        exemple_id: int
):
    exemple: ExempleModel | None = await get_exemple_by_id(
        exemple_id=exemple_id
    )

    if not exemple:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no examples found"
        )

    return exemple
