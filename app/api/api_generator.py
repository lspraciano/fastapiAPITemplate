from fastapi import FastAPI

from app.api.endpoints.router_register import api_routers
from app.api.events.lifespan import lifespan
from app.core.metadata.metadata import get_project_metadata
from app.utils.cors.register_cors import register_cors
from app.utils.exceptions_handlers.register_exceptions_handlers import register_exceptions_handlers
from app.utils.logger.http_logger import register_http_logger
from configuration.configs import settings


def api_factory() -> FastAPI:
    origins: list = ["*"]
    project_metadata: dict = get_project_metadata()

    current_api: FastAPI = FastAPI(
        lifespan=lifespan,
        title=project_metadata["name"],
        description=project_metadata["description"],
        version=project_metadata["version"],
        root_path=settings.ROOT_PATH,
        docs_url=f"/docs",
        redoc_url=f"/redoc",
        openapi_url=f"/openapi.json",
        servers=[
            {
                "url": f"http://localhost:8000",
                "description": "Production environment"
            },
            {
                "url": f"{settings.from_env('production').API_URL_BASE}",
                "description": "Development environment"
            },
        ],
        swagger_ui_parameters={
            "defaultModelsExpandDepth": -1,
            "operationsSorter": "method",
            "filter": True,
            "docExpansion": None,
        },
    )

    register_http_logger(
        app=current_api
    )

    current_api.include_router(
        router=api_routers,
        prefix=f"{settings.API_PREFIX}"
    )

    register_cors(
        app=current_api,
        origins=origins
    )

    register_exceptions_handlers(
        app=current_api
    )

    return current_api
