from fastapi.requests import Request
from starlette.responses import JSONResponse

from ..models import User


async def welcome(request: Request):

    return JSONResponse({"name": "Welcome"})


async def welcome_name(request: Request, name: str):
    return JSONResponse({"name": name})


async def register(request: Request):
    user = await User.create_user(
        username="cenaaa",
        email="tiago.arasilvaaa@gmail.com",
        password="PmDo6ias",
        first_name="tiago",
        last_name="Silva",
    )

    return JSONResponse({"name": user.email})
