# Settings

Python Web Extras comes full equipped with extras that can be added
into any FastAPI application.

---

## Table of Contents

- [Settings](#settings)
    - [Table of Contents](#table-of-contents)
    - [API Settings and Tortoise ORM](#api-settings-and-tortoise-orm)
        - [How to use](#how-to-use)

---

## API Settings and Tortoise ORM

The package is using [FastAPI Utilities](https://fastapi-utils.davidmontague.xyz/)
under the hood to simplify a lot of the process already built in and adds an extra
flavour that allows the clean integration with [Tortoise ORM](https://tortoise.github.io/).

If you do not intend to use Tortoise ORM, this setting can be skipped or else
it can be found [here](./tortoise/models.md)

### How to use

In your settings you will need to import the current `APISettings` class.

**Example:**

```python
# your_settings.py

from python_web_extras.fastapi.api_settings import APISettings

class Settings(APISettings):
    ....

```

[FastAPI Utilities](https://fastapi-utils.davidmontague.xyz/) recommends
the use of a `get_settings()` using `lru_cache()` and this way it would
be simpler to load your enviroment settings in different ways.

A full example is available [here](https://tarsil.github.io/python-web-extras/tests/fastapi/src/core/configs/settings.py).
