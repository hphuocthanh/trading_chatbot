import os
from pydantic_settings import BaseSettings, SettingsConfigDict

# DOTENV = os.path.join(os.path.dirname(__file__), ".env")
# print(DOTENV)


class Settings(BaseSettings):
    OPENAI_API_KEY: str = "OPENAI_API_KEY"
    QDRANT_KEY: str = "QDRANT_KEY"
    SUPABSASE_URL: str = "SUPABSASE_URL"
    SUPABSASE_KEY: str = "SUPABSASE_KEY"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
