# Conf loader

Python Web Extras is unique in it's simplicity of loading dynamic
settings, one of the biggest hurdles of setting up enviroments and
configurations of any project that consumes a lot of time.

---

## Table of Contents

- [Conf loader](#conf-loader)
    - [Table of Contents](#table-of-contents)
    - [Automated load `conf` settings](#automated-load-conf-settings)
        - [Django settings module](#django-settings-module)
            - [Dynamically loading](#dynamically-loading)
        - [Python Web Extras module](#python-web-extras-module)
        - [Dynamically loading](#dynamically-loading-1)
        - [Example](#example)
            - [Dynamically loading](#dynamically-loading-2)
    - [Full working cookiecutter](#full-working-cookiecutter)

---

## Automated load `conf` settings

This package also provides a clean way to load your setting in a very `django` similar fashion.

**Example:**

```python
# views.py

python_web_extras.fastapi.conf import settings

```

Although this is very simple, there is a lot going on here.
Since these package was based on the simplicity of loading modules (coming from django)
we decided to have a similar approach. Let's see:

### Django settings module

Django by default has a `DJANGO_SETTINGS_MODULE` where the default is always
the name of the `project.settings` generated, example `myapp.settings`.

#### Dynamically loading

Django allows to call the manage.py with different settings with two ways.

- Environment variable:

   ```shell
   DJANGO_SETTINGS_MODULE='myapp.development.settings' python manage.py runserver
   ```

- Settings property:

   ```shell
   python manage.py runserver --settings='myapp.development.settings'
   ``` 

### Python Web Extras module

The approach is basically the same as django but we called it `FASTAPI_SETTINGS_MODULE` and it works
exactly the same way when it comes to loading the settings module.

### Dynamically loading

We prefer the loading of settings via environment variables as we believe it's cleaner.

**Example:**

```python
# main.py

# Load the settings from the module
from fastapi import FastAPI

python_web_extras.fastapi.conf import settings

# the rest of the logic for the app
app = FastAPI(**settings.fastapi_kwargs)

```


```shell
FASTAPI_SETTINGS_MODULE='core.development.settings' python app.py
```

The above example is expecting the module location to be passed as a string into
`FASTAPI_SETTINGS_MODULE` or else it will default to `python_web_extras.fastapi.api_settings`.

### Example

An application structure, quite complex and similar to a production ready version.

```shell
└── src
    ├── __init__.py
    ├── apps
    │   ├── __init__.py
    │   └── accounts
    │       ├── __init__.py
    │       ├── models.py
    │       └── v1
    │           ├── __init__.py
    │           ├── routes.py
    │           └── views.py
    ├── core
    │   ├── __init__.py
    │   ├── configs
    │   │   ├── __init__.py
    │   │   ├── databases
    │   │   │   ├── __init__.py
    │   │   │   ├── config.py
    │   │   │   ├── routers.py
    │   │   │   └── settings.py
    │   │   ├── development
    │   │   │   ├── __init__.py
    │   │   │   ├── local_settings.py
    │   │   │   └── settings.py
    │   │   ├── settings.py
    │   │   ├── testing
    │   │   │   ├── __init__.py
    │   │   │   └── settings.py
    │   │   └── urls.py
    └── main.py
```

The application is split by responsabilities and all the settings live inside a `core/configs`
module.

1. `core.configs.settings` - App settings.
2. `core.configs.development.settings` - Development settings.
3. `core.configs.testing.settings` - Testing settings.

Development and testing are inherited from the `main` settings and therefore there is
no reason to replicate existing configurations and keep the codebase clean.

#### Dynamically loading

Using the example above we want to start the environments with the correct settings.

- `main.py` file

    ```python
    # main.py

    # Load the settings from the module
    from fastapi import FastAPI
    python_web_extras.fastapi.conf import settings

    # the rest of the logic for the app
    app = FastAPI(**settings.fastapi_kwargs)

    ```

- Start different environtments.

    ```shell
    FASTAPI_SETTINGS_MODULE='core.configs.development.settings' src.main # Starts the dev settings
    FASTAPI_SETTINGS_MODULE='core.configs.testing.settings' src.main # Starts the testing settings
    FASTAPI_SETTINGS_MODULE='core.configs.settings' src.main # Starts with main settings
    ```

`python_web_extras.fastapi.conf import settings` will know which settings to load by
reading the enviroment variable `FASTAPI_SETTINGS_MODULE` keeping the code clean and
the configurations separated.

## Full working cookiecutter

This package is being already used with a similar approach [here](https://github.com/tarsil/cookiecutter-fastapi).
A cookiecutter already prepared and designed for business.


