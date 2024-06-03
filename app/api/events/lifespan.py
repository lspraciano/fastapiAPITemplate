from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(
        app: FastAPI
):
    print("Running StartUp Events")
    yield
    print("Running ShutDown Events")
