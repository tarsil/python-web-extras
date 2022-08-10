from functools import lru_cache

from ..settings import Settings as MainSettings


class Settings(MainSettings):
    environment: str = 'testing'
    title: str = "Awesome API"
    debug: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
