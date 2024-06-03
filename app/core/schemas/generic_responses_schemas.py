generic_response_400: dict = {
    400: {
        "description": "bad request",
        "content": {"application/json": {"example": {"detail": ["this thing already exists"]}}},
    },
}

generic_response_401: dict = {
    401: {
        "description": "unauthorized",
        "content": {"application/json": {"example": {"detail": ["authentication not valid"]}}},
    },
}

generic_response_403: dict = {
    403: {
        "description": "forbidden",
        "content": {"application/json": {"example": {"detail": ["user not authorized"]}}},
    },
}

generic_response_404: dict = {
    404: {
        "description": "not found",
        "content": {"application/json": {"example": {"detail": ["resource not found"]}}},
    },
}

generic_response_422: dict = {
    422: {
        "description": "unprocessable entity",
        "content": {"application/json": {"example": {"detail": ["field required: name"]}}},
    },
}