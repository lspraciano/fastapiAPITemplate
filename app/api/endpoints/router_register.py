from fastapi import APIRouter

from app.api.endpoints.v1 import v1_api_routers_dict
from app.core.schemas.generic_responses_schemas import generic_response_422, generic_response_404

api_routers_dict_list: list[dict] = [
    v1_api_routers_dict
]

for api_routers_dict in api_routers_dict_list:
    api_routers: APIRouter = APIRouter(
        prefix=api_routers_dict["prefix"]
    )

    for router in api_routers_dict["routers_list"]:
        api_routers.include_router(
            router=router,
            responses={
                **generic_response_404,
                **generic_response_422,
            }
        )
