# Models

This section is dedicated to [Tortoise ORM](https://tortoise.github.io/index.html) integration
with FastAPI and we advise to follow the [installation of tortoise](https://tortoise.github.io/getting_started.html).

---

## Table of Contents

- [Models](#models)
    - [Table of Contents](#table-of-contents)
    - [Motivation](#motivation)
    - [User model](#user-model)
    - [How to use](#how-to-use)
    - [Defaults](#defaults)
    - [Available Models](#available-models)
    - [Working example](#working-example)

---

## Motivation

Tortoise aims to simplify the integration of an ORM into any application in a very
simple fashion and reducing the complexity of designing the models.

Tortoise was based on Django ORM approach of declaring fields, tables and relationships
between tables making the code simpler and cleaner.

Unfortunately Tortoise does not offer, at least not yet, a whole experience of django
when it comes to provide a `User` design approach and this is what we solve.

One of the advantages of this ORM is the full use of `async/await` with the ORM.

## User model

Django is great managing the users internally for their own purposes and middlewares.
Majority of the applications do not need so many built-ins as it can be very opinionated.  

We simply provide a django user like model approach to save time and design
for the applications that need to manage some users as well as provide some
functionalities that allows the creation of a `user` and a `superuser` when needed as well
as hashes the passwords when saving.

## How to use

It's as simple has importing the models into the application.

The `Python Web Extras` user model provides the following fields:

- `id` - IntegerField
- `first_name` - CharField
- `last_name` - CharField
- `username` - CharField
- `email` - CharField
- `password` - CharField
- `last_login` - DatetimeField
- `is_active` - BooleanField
- `is_staff` - BooleanField
- `is_superuser` - BooleanField

Example:

```python
# models.py

from python_web_extras.fastapi.models import User as AbstractUser

class User(AbstractUser):
    class Meta:
        table = "users" # Table name in the database (internally)

```

That is it! The migrations can be run as normal. Since this uses Tortoise ORM,
we recommend their internal migration tool [aerich](https://github.com/tortoise/aerich).

## Defaults

The `AbstractUser` model from the package inherits from the `Model` of Tortoise ORM and therefore
adds the `id` automatically but that can be overriden by another default provided.

Example:

```python

from python_web_extras.fastapi.models import User as AbstractUser
from python_web_extras.fastapi.models import AutoIncrementBigIntMixin, AutoIncrementIntMixin


class User(AutoIncrementBigIntMixin, AbstractUser):
    class Meta:
        table = "users" # Table name in the database (internally)


class User(AutoIncrementIntMixin, AbstractUser): # Same as the default of the Model `id`.
    class Meta:
        table = "users" # Table name in the database (internally)

```

## Available Models

1. `AbstractUser` - User table model.
2. `AutoIncrementBigIntMixin` - Add a `bigint` id into the model.
3. `AutoIncrementIntMixin` - Add an `int` id into the model.

## Working example

An example of this approach can be found [here](https://github.com/tarsil/cookiecutter-fastapi/blob/main/%7B%7B%20cookiecutter.project_root_name%20%7D%7D/%7B%7B%20cookiecutter.project_src_name%20%7D%7D/apps/accounts/models.py)
