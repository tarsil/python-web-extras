import importlib
import os

from loguru import logger

from .api_settings import APISettings


def get_settings(config: str = None) -> APISettings:
    """
    The `config` is a module path in teh format of `python_web_extras.fastapi.api_settings`
    or else it will load the default.
    """
    module = (
        os.getenv("FASTAPI_SETTINGS_MODULE") or "python_web_extras.fastapi.api_settings"
    )

    try:
        config = config or module
        configs = importlib.import_module(config)
    except (ImportError, AttributeError):
        configs = importlib.import_module(module)

    settings = getattr(configs, "get_settings", None)
    if not settings:
        logger.warning(f"get_settings() not found in {module}.")
        logger.warning("Default to base APISettings.")
        settings = APISettings

    return settings()


settings = get_settings()
