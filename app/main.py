from fastapi import FastAPI

from app.api import simple_api

app = FastAPI()

app.include_router(simple_api.router)