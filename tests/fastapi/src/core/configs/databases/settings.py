import os
import sys
from pathlib import Path

from .config import TORTOISE_ORM

Path(__file__).resolve().parent.parent.parent.parent.parent
SITE_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
)
sys.path.append(SITE_ROOT)
sys.path.append(os.path.join(SITE_ROOT, "apps"))

DATABASES = TORTOISE_ORM
