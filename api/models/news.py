from dataclasses import Field


class News:
    title: str = Field(min_length=1, max_length=1000)
    description: str = Field(default=None, max_length=4096)
