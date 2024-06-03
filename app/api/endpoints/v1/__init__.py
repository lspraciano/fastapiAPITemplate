from app.api.endpoints.v1 import root, exemple

v1_api_routers_dict: dict = {
    "prefix": "/v1",
    "routers_list": [
        root.router,
        exemple.router
    ]
}
