from fastapi import status, HTTPException

unique_key_errors_constant_text: str = "some of the provided values already exist in the database"


def raise_unique_keys_error(
        error_text: str
) -> None:
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=[
            unique_key_errors_constant_text,
            error_text
        ]
    )
