from typing import List

from fastapi_utils.api_settings import APISettings as FastAPISettings


class APISettings(FastAPISettings):
    """
    Extra properties used for the configurations of the app.
    """

    @property
    def fast_api_utils_password_hashers(self) -> list:
        return [
            "core.lib.contrib.auth.hashers.PBKDF2PasswordHasher",
            "core.lib.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        ]
