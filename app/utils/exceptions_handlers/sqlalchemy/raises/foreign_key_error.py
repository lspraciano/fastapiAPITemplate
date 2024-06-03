from fastapi import status, HTTPException

foreign_key_errors_constant_text: str = "the value entered for foreign key does not exist"


def raise_foreign_key_error(
        error_text: str
) -> None:
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=[
            foreign_key_errors_constant_text,
            error_text
        ]
    )
