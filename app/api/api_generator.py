from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.events.shutdown.register_shutdown_events import register_shutdown_events
from app.api.events.startup.register_startup_events import register_startup_events
from app.core.metadata.metadata import get_project_metadata
from app.api.endpoints.router_register import api_routers
from configuration.configs import settings


def api_factory() -> FastAPI:
    origins: list = ["*"]
    project_metadata: Dict = get_project_metadata()

    current_api: FastAPI = FastAPI(
        title=project_metadata["name"],
        description=project_metadata["description"],
        version=project_metadata["version"],
        docs_url=f"{settings.API_URL}/docs",
        redoc_url=f"{settings.API_URL}/redoc",
        openapi_url=f"{settings.API_URL}/openapi.json",
        servers=[
            {
                "url": f"http://localhost:8000",
                "description": "Production environment"
            },
            {
                "url": f"http://127.0.0.1:8000",
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

    current_api.include_router(
        api_routers,
        prefix=f"{settings.API_URL}"
    )

    current_api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["Detections"]
    )

    current_api: FastAPI = register_startup_events(
        api=current_api
    )

    current_api: FastAPI = register_shutdown_events(
        api=current_api
    )

    return current_api
