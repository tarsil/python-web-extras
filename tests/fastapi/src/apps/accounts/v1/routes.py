"""
Routes responsible the urls of the current namespace and imported in `.routes`.
"""

from fastapi.routing import APIRouter

from .views import register, welcome, welcome_name

router = APIRouter(
    prefix="/api/v1",
    tags=["my-fastapi-app"],
    responses={404: {"description": "Not Found"}},
)
router.add_api_route("/", welcome)
router.add_api_route("/{name}", welcome_name)


accounts = APIRouter(
    prefix="/api/v1/accounts",
    responses={404: {"description": "Not Found"}},
)
accounts.add_api_route("/register", welcome)
