# Logging

Logging an application is a must and not a nice to have and mostly due
to the errors that constantly happen during development time.

---

## Table of Contents

- [Logging](#logging)
    - [Table of Contents](#table-of-contents)
    - [InterceptHandler](#intercepthandler)
        - [How to use it](#how-to-use-it)
    - [Working example](#working-example)

---

## InterceptHandler

As mentioned before, if not, please check [API Settings](./settings.md),
`Python Web Extras` uses [FastAPI Utilities](https://fastapi-utils.davidmontague.xyz/)
under the hood and therefore uses some of it's practices, more precisely
the `get_settings()`.

### How to use it

To apply the interceptor, we recommend to add it into the base settings.

**Example:**

```python

from loguru import logger
from python_web_extras.fastapi.api_settings import APISettings
from python_web_extras.fastapi.logging import InterceptHandler


class Settings(APISettings):
    ...
    ...


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

```

From now on when the app starts with these settings, it will have the
`InterceptHandler` embed and operational.

## Working example

An example of this approach can be found [here](https://github.com/tarsil/cookiecutter-fastapi/blob/main/%7B%7B%20cookiecutter.project_root_name%20%7D%7D/%7B%7B%20cookiecutter.project_src_name%20%7D%7D/core/configs/settings.py).
