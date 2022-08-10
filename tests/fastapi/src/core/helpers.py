# Copyright (c) 2021 Tiago Silva <https://github.com/tarsil>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import datetime
import functools
import json
import threading
from collections import namedtuple

import pytz

_apps_lock = threading.RLock()
_apps = {}

__author__ = "Tiago A. Silva <tiago.arasilva@gmail.com>"
__version__ = "1.0.1"


class BaseClass:
    """
    This class serves with the purpose of dynamically create a constructor and override the default
    __eq__ operator from python allowing the direct comparison between python objects
    """

    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])

    def __eq__(self, instance):
        if not isinstance(instance, self.__class__):
            return False
        if hash(frozenset(self.__dict__.items())) == hash(
            frozenset(instance.__dict__.items())
        ):
            return True
        return False

    def __ne__(self, instance):
        if not isinstance(instance, self.__class__):
            return True
        if hash(frozenset(self.__dict__.items())) != hash(
            frozenset(instance.__dict__.items())
        ):
            return True
        return False

    @property
    def utc(self):
        utc_now = pytz.utc.localize(datetime.datetime.utcnow())
        return utc_now

    def __repr__(self):
        return "<%s - %s />" % (self.__class__.__name__, self.utc)


class Slot2Object:
    """
    Class that converts a dict into a object using slots.
    Performance wise, is faster and gives a better memory usage.

    Usage:
    _dict = {'a': 1, 'b': {'c': 1}}
    s = Slot2Object(_dict)

    Result:
        s.a
        1

        s.b
        {'c': 1}
    """

    __slots__ = ["__dict__"]

    def __init__(self, __dict__):
        self.__dict__ = __dict__

    def __getitem__(self, item):
        return getattr(self, item)


def json_2object(json_payload):
    """
    Returns a Python type object from a json type
    :param json_payload: Json to be converted
    :return: Python object
    """
    return json.loads(
        json_payload,
        object_hook=lambda d: namedtuple("X", list(d.keys()))(*list(d.values())),
    )


def rgetattr(obj, attr, *args):  # pragma no cover
    """
    A replacement of the default getattr() with a nuance of getting the nested values from objects
    :param obj: Object to lookup
    :param attr: Attribute to search
    :param args: Defaut value
    :return: Value
    """

    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split("."))


class SlotObject:
    """
    Class that converts a dict into an object using slots.
    Performance wise, is faster and gives a better memory usage.
    This class provides a nested setattr.

    Usage:
        _dict = {'a': 1, 'b': {'c': 1}}
        s = SlotObject(_dict)

    Result:
        s.a
        1

        s.b.c
        1
    """

    __slots__ = ["__dict__"]

    def __init__(self, __dict__):
        for k, v in __dict__.items():
            setattr(self, k, self.__class__(v)) if isinstance(
                v, dict
            ) and v else setattr(self, k, v)

    def __getitem__(self, item):
        return getattr(self, item)


def remove_prefix(text, prefix):
    """
    In python 3.9 there is already a native function to remove the prefixes.
    See https://www.python.org/dev/peps/pep-0616/
    If the version is inferior to 3.9 then runs the below solution.
    """
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def set_app(app):
    """Sets an App instance by a given name.

    Example:
        ```
        from flask_apscheduler import APScheduler

        try:
            get_app(APScheduler.__name__)
        except ValueError:
            scheduler = APScheduler()
            scheduler.init_app(app)
            set_app(scheduler)
        ```

    Args:
        app: App module added to the application context.

    Returns:
        App: The app instance with the given name
    """
    with _apps_lock:
        if app.__class__.__name__ not in _apps:
            _apps[app.__class__.__name__] = app
            return app


def get_app(name: str):
    """Retrieves an App instance by name.

    Args:
      name: Name of the App instance to retrieve (optional).

    Returns:
      App: An App instance with the given name.

    Raises:
      ValueError: If the specified name is not a string, or if the specified
          app does not exist.
    """
    if not isinstance(name, str):
        raise ValueError(
            'Illegal app name argument type: "{}". App name '
            "must be a string.".format(type(name))
        )
    with _apps_lock:
        if name in _apps:
            return _apps[name]

    raise ValueError(
        (
            'The app named "{name}" does not exist. Make sure to initialize '
            "the app by calling init_app() or App(app) with your app name as the "
            "argument."
        ).format(name=name)
    )
