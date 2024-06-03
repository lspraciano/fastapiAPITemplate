from fastapi import FastAPI

from app.api.api_generator import api_factory
from configuration.configs import settings

app: FastAPI = api_factory()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="warning",
        reload=settings.SERVER_RELOAD,
    )
