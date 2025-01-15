from os import getenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    PINECODE_API_KEY: str
    APP_ENV: str
    LANGCHAIN_TRACING_V2: bool
    LANGCHAIN_ENDPOINT: str
    LANGCHAIN_API_KEY: str
    LANGCHAIN_PROJECT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings(
    APP_ENV=getenv("APP_ENV", "development"),
    OPENAI_API_KEY=getenv("OPENAI_API_KEY", ""),
    PINECODE_API_KEY=getenv("PINECODE_API_KEY", ""),
    LANGCHAIN_TRACING_V2=(getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"),
    LANGCHAIN_ENDPOINT=getenv("LANGCHAIN_ENDPOINT", ""),
    LANGCHAIN_API_KEY=getenv("LANGCHAIN_API_KEY", ""),
    LANGCHAIN_PROJECT=getenv("LANGCHAIN_PROJECT", ""),
)
