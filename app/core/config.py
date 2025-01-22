"""
Configuration module for application settings.

This module defines and loads environment variables and application settings
using Pydantic's BaseSettings.
"""

from pydantic_settings import BaseSettings
from pydantic import SecretStr


class Settings(BaseSettings):
    """
    Settings class that defines and loads application configuration.

    Environment variables and default values are defined here using Pydantic's BaseSettings.
    """

    APP_ENV: str = "development"
    LANGCHAIN_API_KEY: str = "langchain_api_key"
    LANGCHAIN_ENDPOINT: str = "langchain_endpoint"
    LANGCHAIN_PROJECT: str = "langchain_project"
    LANGCHAIN_TRACING_V2: bool = False
    OPENAI_API_KEY_GH: SecretStr = SecretStr("openai_api_key_gh")
    OPENAI_API_KEY: str = "openai_api_key"
    PINECODE_API_KEY: str = "pinecode_api_key"
    ALLOW_ORIGINS: str = "http://localhost:4321"

    class Config:
        """
        Configuration for the Settings class, including case sensitivity and
        .env file handling.
        """

        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
