import json
import logging
import time
import traceback
import uuid
from typing import Callable

from fastapi import FastAPI
from fastapi import Request, Response

from app.utils.logger.configure_logger import configure_http_logger

http_logger: logging.Logger = configure_http_logger()


def register_http_logger(
        app: FastAPI
) -> None:
    @app.middleware("http")
    async def api_logging(
            request: Request,
            call_next: Callable
    ) -> Response:
        start_time: float = time.time()

        try:
            response: Response = await call_next(request)

            log_message: dict = {
                "status_code": response.status_code,
                "method": request.method,
                "host": request.url.hostname,
                "endpoint": request.url.path,
                "processing_time_seconds": round(time.time() - start_time, 4),
                "headers": dict(request.headers),
            }

            http_logger.info(
                msg=log_message
            )

            return response

        except Exception as error:
            trace_id: str = str(uuid.uuid4())
            http_logger.critical(
                msg={
                    "trace_id": trace_id,
                    "error": str(error),
                    "type": str(type(error)),
                    "traceback": traceback.format_exc(),
                }
            )

            return Response(
                status_code=500,
                content=json.dumps(
                    {
                        "detail": [
                            "unexpected error. contact support",
                            f"trace_id: {trace_id}",
                            str(error)
                        ],
                    }
                ),
                media_type="application/json"
            )
