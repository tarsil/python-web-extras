"""
All the custom settings are placed here. The settings are therefore loaded
trough environment variable `FASTAPI_SETTINGS_FILENAME` that should be just a location
of the file.
"""
import ast
import binascii
import logging
import os
import sys
from functools import lru_cache
from typing import List

from loguru import logger
from python_web_extras.fastapi.api_settings import APISettings
from python_web_extras.fastapi.logging import InterceptHandler


class Settings(APISettings):
    """
    Base settings for the FastApi app
    """

    environment: str = "production"
    debug: bool = False
    title: str = "Awesome API"
    email_admin: str = "foobar@example.com"
    description: str = "My new fastapi app"
    port: int = 8001
    host: str = "0.0.0.0"
    reload: bool = False
    secret_key = os.getenv("SECRET_KEY", binascii.hexlify(os.urandom(24)))

    # DATABASE
    database_url: str = os.getenv("DB_CONNECTION", None)
    max_connection_count: int = os.getenv("MAX_CONNECTIONS_COUNT", 10)
    min_connection_count: int = os.getenv("MIN_CONNECTIONS_COUNT", 10)

    # ALLOWED HOSTS
    allowed_hosts: List[str] = ast.literal_eval(os.getenv("ALLOWED_HOSTS", "[]"))


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    configure_logger(settings)
    return settings


def configure_logger(settings: Settings) -> None:
    logging_level = logging.DEBUG if settings.debug else logging.INFO
    loggers = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in loggers:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler(level=logging_level)]

    logger.configure(handlers=[{"sink": sys.stderr, "level": logging_level}])
