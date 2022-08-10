import os
import sys
from pathlib import Path

from fastapi_utils.api_settings import APISettings, get_api_settings
from loguru import logger
from python_web_extras.fastapi.errors.http_error import http_error_handler
from python_web_extras.fastapi.errors.validation_error import http422_error_handler
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.utils import get_openapi


def build_path():
    """
    Builds the path of the project and project root.

    Exports the folders on the
    """
    Path(__file__).resolve().parent.parent
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

    if not SITE_ROOT in sys.path:
        sys.path.append(SITE_ROOT)
        sys.path.append(os.path.join(SITE_ROOT, "apps"))


def configure_app(app: FastAPI, settings: APISettings) -> None:
    """
    The configuration is read from the filename in the "FASTAPI_SETTINGS_MODULE"
    environment variable (if it exists) and some other important settings.

    We activate the routing here to make sure everything runs smoothly but some additional configurations can also
    be added.

    :param FastAPI app: The FastAPI app that requires configuring.
    :return: None
    """

    from core.configs.urls import router as router_v1
    from core.events import create_start_app_handler, create_stop_app_handler

    app.include_router(router_v1)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    try:
        app.add_event_handler("startup", create_start_app_handler(app))
        app.add_event_handler("shutdown", create_stop_app_handler(app))
    except Exception as e:
        logger.exception(e)

    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, http422_error_handler)


def get_settings(config: str = None):
    """
    The `config` is a module path in the format of `core.configs.settings` or else it will load the default.
    """
    from core.conf import settings

    return settings


def custom_openapi():
    settings = get_settings()
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.title,
        version="1.0.0",
        description=settings.description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


def get_application(config: str = None):
    """
    Main entry-point of the application.
    Initializes the service and all of the dependencies.

    1. Builds the project path. Inspired by the way Django manages the settings
    from the relative path.
    2. Clears the settings cache.
    3. Loads the settings sent to the project via file or module string location.
    4. Creates the FastAPI app object.
    5. Initializes the dependencies and add them to the application context.
    """
    build_path()
    get_api_settings.cache_clear()
    settings = get_settings(config)

    app = FastAPI(**settings.fastapi_kwargs)
    configure_app(app, settings)

    # OPEN API SCHEMA - app.openapi = custom_openapi
    setattr(app, "openapi", custom_openapi)
    return app


app = get_application()
