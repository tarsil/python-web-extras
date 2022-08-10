# Hashers

Hashing passwords is the utmost important task when storing
sensitive user information in the database.

---

## Table of Contents

---

## API Settings

[In this section](../settings.md) we mentioned the API Settings if using the
integration with [Tortoise ORM](https://tortoise.github.io/index.html) and this is
the reason.

`Python Web Extras` provides already some hashing algorightms as default for the passwords.

## Defaults

```python
# your_settings.py

from python_web_extras.fastapi.api_settings import APISettings

class Settings(APISettings):

    @property
    def fast_api_utils_password_hashers(self) -> list:
        return [
            "python_web_extras.contrib.auth.hashers.PBKDF2PasswordHasher",
            "python_web_extras.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
        ]
```

When using the [User](./models.md#user-model) from the package, it will call
the above settings and use these hashing modules to generate a secure password.

## Custom Hashing

It is possible to add your custom hashing into the system as well.

**Example**:

- **hashers.py**

    ```python
    # hashers.py
    from python_web_extras.contrib.auth.hashers import PBKDF2PasswordHasher

    class MyCustomPBKDF2Hasher(PBKDF2PasswordHasher):
        iterations = 4000000
    ```

- **settings.py**

    ```python
    from python_web_extras.fastapi.api_settings import APISettings


    class Settings(APISettings):

        @property
        def fast_api_utils_password_hashers(self) -> list:
            return [
                "hashers.MyCustomPBKDF2Hasher",
                "python_web_extras.contrib.auth.hashers.PBKDF2PasswordHasher",
                "python_web_extras.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
            ]

    ```

## Considerations

The package uses [passlib](https://passlib.readthedocs.io/en/stable/) for the hashing.
