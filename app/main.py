from fastapi import FastAPI

from app.api.api_generator import api_factory
from configuration.configs import settings

app: FastAPI = api_factory()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="info",
        reload=settings.SERVER_RELOAD == 1,
    )
