# pragma: no cover
from python_web_extras.contrib.auth.tortoise.base_user import AbstractUser as User
from python_web_extras.contrib.auth.tortoise.base_user import (
    AutoIncrementBigIntMixin,
    AutoIncrementIntMixin,
)

from .hashers import check_password, is_password_usable, make_password
