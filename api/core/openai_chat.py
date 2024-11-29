from .settings import settings
from openai import OpenAI

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,  # This is the default and can be omitted
)


def get_openai():
    print("OpenAI client created")
    return client
