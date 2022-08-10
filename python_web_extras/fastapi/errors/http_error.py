"""
Error handlers that can be used in the middleware of any
fastapi application. E.g.:

Example:
    from fastapi.exceptions import RequestValidationError
    from starlette.exceptions import HTTPException
    from python_web_extras.fastapi.errors.http_error import http_error_handler
    from python_web_extras.fastapi.errors.validation_error import http422_error_handler

    app = FastAPI(__name__)

    app.add_exception_handler(HTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, http422_error_handler)
"""

from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse({"errors": [exc.detail]}, status_code=exc.status_code)
