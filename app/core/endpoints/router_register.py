from fastapi import APIRouter

from app.core.endpoints.v1 import root, exemple

api_routers: APIRouter = APIRouter()

api_routers.include_router(
    root.router,
)

api_routers.include_router(
    exemple.router,
)
