from functools import lru_cache
from typing_extensions import Annotated
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

from api.core.settings import Settings

from .routes import chat

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_v1 = FastAPI()
api_v1.include_router(chat.router)

app.mount("/v1", api_v1)


@lru_cache()
def get_settings():
    return Settings()


openai.api_key = get_settings().OPENAI_API_KEY


@app.get("/")
def read_root():
    return {"Hello": "World"}
