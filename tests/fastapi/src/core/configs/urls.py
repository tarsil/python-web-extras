"""
Main module for the routes of the app.
Imports all the remaining modules routes via `import` module name
"""

from accounts.v1.routes import accounts as accounts_router
from accounts.v1.routes import router as router_v1
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()
router.include_router(router_v1)
router.include_router(accounts_router)
