from fastapi import FastAPI
from .routes import chat

app = FastAPI()


app.include_router(chat.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}