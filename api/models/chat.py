# Shared properties
from dataclasses import Field


class ChatPayload:
    user_id: str = Field(min_length=1, max_length=255)
    user_prompt: str = Field(default=None, max_length=4096)
