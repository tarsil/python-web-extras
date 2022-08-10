# pragma no cover
import functools
import sys
import warnings

from python_web_extras.contrib.auth.hashers import (
    check_password,
    get_hasher,
    get_hashers_by_algorithm,
    get_random_string,
    identify_hasher,
    is_password_usable,
    make_password,
    must_update_salt,
)
from python_web_extras.contrib.exceptions import ImproperlyConfigured
from python_web_extras.contrib.utils.module_loading import import_string

from .conf import settings


@functools.lru_cache
def get_hashers():
    hashers = []
    if not hasattr(settings, "fast_api_utils_password_hashers"):
        warnings.warn("Property fast_api_utils_password_hashers missing from settings.")
        return hashers

    for hasher_path in settings.fast_api_utils_password_hashers:
        hasher_cls = import_string(hasher_path)
        hasher = hasher_cls()
        if not getattr(hasher, "algorithm"):
            raise ImproperlyConfigured(
                "hasher doesn't specify an algorithm name: %s" % hasher_path
            )
        hashers.append(hasher)
    return hashers


sys.modules["python_web_extras.contrib.auth.hashers"].get_hashers = get_hashers
