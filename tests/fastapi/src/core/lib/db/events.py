from fastapi import FastAPI
from loguru import logger
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from ...configs.databases.config import TORTOISE_ORM


async def connect_to_db(app: FastAPI) -> None:
    logger.info("Connecting to database")
    register_tortoise(
        app=app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )

    logger.info("Connection established")


async def close_db_connection(app: FastAPI) -> None:
    logger.info("Closing connection to database")

    await Tortoise.close_connections()

    logger.info("Connection closed")
