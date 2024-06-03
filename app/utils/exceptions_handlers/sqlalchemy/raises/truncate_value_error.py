from fastapi import status, HTTPException

truncate_field_errors_constant_text: str = "the provided value exceeds the permitted limit"


def raise_truncate_value_error(
        error_text: str
) -> None:
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=[
            truncate_field_errors_constant_text,
            error_text
        ]
    )
