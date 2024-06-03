import json
import logging
import time
from typing import Callable

from fastapi import FastAPI
from fastapi import Request, Response
from starlette.responses import StreamingResponse

from app.utils.logger.configure_logger import configure_logger

logger: logging.Logger = configure_logger()


def register_http_logger(
        app: FastAPI
) -> None:
    @app.middleware("http")
    async def api_logging(
            request: Request,
            call_next: Callable
    ) -> Response:
        start_time: time.time = time.time()

        try:
            response: Response | StreamingResponse = await call_next(request)
            response_body: bytes = b""
            async for chunk in response.body_iterator:
                response_body += chunk
            log_message: dict = {
                "status_code": response.status_code,
                "method": request.method,
                "host": request.url.hostname,
                "endpoint": request.url.path,
                "processing_time_seconds": round(time.time() - start_time, 4),
                "response": response_body.decode(),
                "headers": dict(request.headers),
            }

            logger.info(
                msg=log_message
            )
        except Exception as error:
            logger.error(
                msg=f"this error needs to be handled: {error} type: {type(error)}"
            )

            return Response(
                status_code=500,
                content=json.dumps(
                    {
                        "detail": [
                            "unexpected error. contact support",
                            str(error)
                        ]
                    }
                ),
                media_type="application/json"
            )

        return Response(
            content=response_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
