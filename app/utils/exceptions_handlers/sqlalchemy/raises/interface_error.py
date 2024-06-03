from fastapi import status, HTTPException

interface_errors_constant_text: str = "data source name not found and no default driver specified"


def raise_interface_error(
        error_text: str
) -> None:
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=[
            interface_errors_constant_text,
            error_text
        ]
    )
