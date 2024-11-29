# Shared properties
from typing import Iterable
from pydantic import BaseModel, Field
from openai.types.chat import ChatCompletionMessageParam


class ChatPayload(BaseModel):
    # make user_id optional
    # user_id: str = Field(min_length=1, max_length=255)
    user_id: str = Field(min_length=1, max_length=255, default=None)
    coin_id: str = Field(min_length=1, max_length=50)
    messages: Iterable[ChatCompletionMessageParam]
