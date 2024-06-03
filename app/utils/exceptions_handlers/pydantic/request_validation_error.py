from typing import Any

from fastapi import status, Request
from fastapi.responses import JSONResponse


def request_validation_exception_handler(
        request: Request,
        exception: Exception | Any
):
    messages: list = []

    for error in exception.errors():
        message: str = f"{error['msg']}: {error['loc'][-1]}"
        messages.append(message)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": messages
        }
    )
