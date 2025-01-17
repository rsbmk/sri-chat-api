from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    APP_ENV: str = "development"
    LANGCHAIN_API_KEY: str = "langchain_api_key"
    LANGCHAIN_ENDPOINT: str = "langchain_endpoint"
    LANGCHAIN_PROJECT: str = "langchain_project"
    LANGCHAIN_TRACING_V2: bool = False
    OPENAI_API_KEY_GH: SecretStr = SecretStr("openai_api_key_gh")
    OPENAI_API_KEY: str = "openai_api_key"
    PINECODE_API_KEY: str = "pinecode_api_key"

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
