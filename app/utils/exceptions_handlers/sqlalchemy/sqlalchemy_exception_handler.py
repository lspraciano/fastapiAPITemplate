from typing import Callable, Any

from fastapi import Request

from app.utils.exceptions_handlers.sqlalchemy.raises.foreign_key_error import raise_foreign_key_error
from app.utils.exceptions_handlers.sqlalchemy.raises.interface_error import raise_interface_error
from app.utils.exceptions_handlers.sqlalchemy.raises.truncate_value_error import raise_truncate_value_error
from app.utils.exceptions_handlers.sqlalchemy.raises.unique_keys_error import raise_unique_keys_error

erros_dict: dict = {
    "UNIQUE": raise_unique_keys_error,
    "Truncated value": raise_truncate_value_error,
    "FOREIGN": raise_foreign_key_error,
    "ODBC": raise_interface_error,
}


def get_sqlalchemy_exception(
        error_text: str
) -> None:
    for key in erros_dict:
        lower_case_key_name: str = key.lower()
        lower_case_error_text: str = error_text.lower()

        if lower_case_key_name in lower_case_error_text:
            function: Callable = erros_dict[key]
            function(error_text=error_text)


def sqlalchemy_exception_handler(
        request: Request,
        exception: Exception | Any
):
    get_sqlalchemy_exception(
        error_text=exception.args[0]
    )
