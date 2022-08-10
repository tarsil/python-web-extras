from typing import Type

from tortoise.models import Model


class DefaultRouter:
    def db_for_read(self, model: Type[Model]):
        return "default"

    def db_for_write(self, model: Type[Model]):
        return "default"


TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "localhost",
                "port": "5432",
                "user": "postgres",
                "password": "postgres",
                "database": "fastapi",
            },
        },
    },
    "apps": {
        "accounts": {
            "models": ["accounts.models", "aerich.models"],
            "connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}
