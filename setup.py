#!/usr/bin/env python3
import os
import re
import shutil
import sys
from io import open

from setuptools import find_packages, setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)

# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of Python Web Extra requires Python {}.{}, but you're trying
to install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install python_web_extras
This will install the latest version of Python Web Extra which works on
your version of Python. If you can't upgrade your pip (or Python), request
an older version of Python Web Extra.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)


def read(f):
    return open(f, "r", encoding="utf-8").read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("python_web_extras")

setup(
    name="python_web_extras",
    version=version,
    url=" https://tarsil.github.io/fastapi-utils-extra/",
    license="MIT",
    description="Utils for your favourite python web projects.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Tiago Silva",
    author_email="tiago.arasilva@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        "fastapi>=0.79.0",
        "fastapi_utils>=0.2.1",
        "loguru>=0.6.0",
        "quart>=0.18.0",
        "passlib==1.7.4",
        "pytz==2022.1",
        "tortoise-orm>=0.19.2",
    ],
    python_requires=">=3.7",
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
