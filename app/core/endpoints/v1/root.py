from typing import Dict

from fastapi import APIRouter, status

from app.core.metadata.metadata import get_project_metadata
from app.core.schemas.root_schemas import RootResponse

router = APIRouter(
    tags=["Root"],
    prefix=""
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=RootResponse
)
async def check_metadata_():
    project_metadata: Dict = get_project_metadata()
    return {
        "status": "online",
        **project_metadata
    }
