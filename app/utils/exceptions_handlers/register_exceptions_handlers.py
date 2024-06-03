from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError as FastAPIRequestValidationError
from sqlalchemy.exc import IntegrityError as SqlAlchemyIntegrityError
from sqlalchemy.exc import InterfaceError as SqlAlchemyInterfaceError
from sqlalchemy.exc import ProgrammingError as SqlAlchemyProgrammingError

from app.utils.exceptions_handlers.pydantic.request_validation_error import request_validation_exception_handler
from app.utils.exceptions_handlers.sqlalchemy.sqlalchemy_exception_handler import sqlalchemy_exception_handler


def register_exceptions_handlers(
        app: FastAPI
):
    app.add_exception_handler(
        exc_class_or_status_code=FastAPIRequestValidationError,
        handler=request_validation_exception_handler
    )

    app.add_exception_handler(
        exc_class_or_status_code=SqlAlchemyIntegrityError,
        handler=sqlalchemy_exception_handler
    )

    app.add_exception_handler(
        exc_class_or_status_code=SqlAlchemyProgrammingError,
        handler=sqlalchemy_exception_handler
    )

    app.add_exception_handler(
        exc_class_or_status_code=SqlAlchemyProgrammingError,
        handler=sqlalchemy_exception_handler
    )

    app.add_exception_handler(
        exc_class_or_status_code=SqlAlchemyInterfaceError,
        handler=sqlalchemy_exception_handler
    )
