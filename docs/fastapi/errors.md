# Error Handling

Handling errors in an application is another must.
The errors can be added into the middleware of any
FastAPI application.

---

## Table of Contents

- [Error Handling](#error-handling)
    - [Table of Contents](#table-of-contents)
    - [http_error_handler](#http_error_handler)
    - [http422_error_handler](#http422_error_handler)
    - [Working example](#working-example)

---

## http_error_handler

**Example:**

```python
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from python_web_extras.fastapi.errors.http_error import http_error_handler

app = FastAPI(__name__)

app.add_exception_handler(HTTPException, http_error_handler)

```

## http422_error_handler

**Example:**

```python
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from python_web_extras.fastapi.errors.validation_error import http422_error_handler

app = FastAPI(__name__)

app.add_exception_handler(RequestValidationError, http422_error_handler)

```

## Working example

An example of this approach can be found [here](https://github.com/tarsil/cookiecutter-fastapi/blob/main/%7B%7B%20cookiecutter.project_root_name%20%7D%7D/%7B%7B%20cookiecutter.project_src_name%20%7D%7D/main.py#L30).
