# Python Web Extras

[![Build and Publish](https://github.com/tarsil/python-web-extras/actions/workflows/main.yml/badge.svg)]((https://github.com/tarsil/python-web-extras/actions/workflows/main.yml/badge.svg))

**Official Documentation** - <https://tarsil.github.io/python-web-extras>

---

## Table of Contents

- [Python Web Extras](#python-web-extras)
  - [Table of Contents](#table-of-contents)
  - [About Python Web Extras](#about-python-web-extras)
  - [Tortoise ORM](#tortoise-orm)
    - [Overview](#overview)
      - [Supported Django and Python Versions](#supported-django-and-python-versions)
    - [Installation](#installation)
  - [Documentation and Support](#documentation-and-support)
  - [License](#license)

---

## About Python Web Extras

Python Web Extras is a miscellaneous of common utilities for FastAPI, Quart
and future integrations with other frameworks.

The aim is to make the life of developers simpler when it comes to
some configurations.

`Python Web Extras` also brings extra integrations with [Tortoise ORM](https://tortoise.github.io/index.html).

Tortoise offers a way of integrating models into any application without a lot
of configurations previously faced with others (SQLAlchemy, for instance) and for
those familiar with [Django](https://www.djangoproject.com/), then Tortoise is a brise.

## Tortoise ORM

When building an application that manages users, Django offers
an out of the box built-in User models that can be very useful within the
whole set of dependencies. Tortoise ORM is a bit less opinionated regarding those
and therefore `Python Web Extras` offers a similar abstraction based Django
where a `create_user` and `create_super_user` as well as password
hashing are handled by simply inheriting from the base user model.

### Overview

#### Supported Django and Python Versions

| Python |
| --------------- |
| 3.8             |
| 3.9             |
| 3.10            |

### Installation

To install python-web-extras:

```shell
pip install python-web-extras
```

## Documentation and Support

Full documentation for the project is available at <https://tarsil.github.io/python-web-extras/>

## License

Copyright (c) 2022-present Tiago Silva and contributors under the [MIT license](https://opensource.org/licenses/MIT).
