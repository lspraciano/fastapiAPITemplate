from fastapi import FastAPI

from app.api.api_generator import api_factory

app: FastAPI = api_factory()
