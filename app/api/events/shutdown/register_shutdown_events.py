from typing import Callable

from fastapi import FastAPI


def register_shutdown_events(
        api: FastAPI,
        functions: list[Callable] | None = None
) -> FastAPI:
    @api.on_event("shutdown")
    async def shutdown():
        if not functions:
            return

        for function in functions:
            function()

    return api
