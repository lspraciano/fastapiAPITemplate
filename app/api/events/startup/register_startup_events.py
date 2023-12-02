from typing import Callable

from fastapi import FastAPI

from configuration.configs import settings


def register_startup_events(
        api: FastAPI,
        functions: list[Callable] | None = None
) -> FastAPI:
    @api.on_event("startup")
    async def startup():
        print(f"Running Mode: {settings.APP_RUNNING_MODE}")

        if not functions:
            return

        for function in functions:
            function()

    return api
