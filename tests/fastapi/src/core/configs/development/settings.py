from functools import lru_cache
from typing import List

from ..settings import Settings as MainSettings
from ..settings import configure_logger


class Settings(MainSettings):
    environment: str = "development"
    title: str = "Awesome API - Development"
    debug: bool = True
    port: int = 8002
    reload: bool = True
    host = "0.0.0.0"

    # ALLOWED HOSTS
    database_url: str = "postgres://postgres:postgres@localhost:5432/fastapi"
    allowed_hosts: List[str] = ["*"]


@lru_cache()
def get_settings() -> Settings:
    try:
        from .local_settings import Settings as LocalSettings

        settings = LocalSettings()
    except ImportError:
        settings = Settings()

    configure_logger(settings)
    return settings
