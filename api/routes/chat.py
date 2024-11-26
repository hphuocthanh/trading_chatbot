from fastapi import APIRouter
from fastapi.responses import (
    StreamingResponse,
)
from api.models.chat import ChatPayload
import openai
import gnews

router = APIRouter(tags=["chat"])


@router.post("/chat", response_class=StreamingResponse)
async def chat(chat_payload: ChatPayload):
    return [{"username": "Rick"}, {"username": "Morty"}]
