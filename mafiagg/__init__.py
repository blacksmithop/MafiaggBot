"""
Mafiag GG API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Mafia API.

:copyright: (c) 2021-present blacksmithop
:license: MIT, see LICENSE for more details.

"""

__title__ = "mafiagg"
__author__ = "blacksmithop"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present blacksmithop"
__version__ = "1.0.3"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .client import *
from .decks import *
from .roles import *
from .room import *
from .settings import *
from .setups import *
from .user import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=1, minor=0, micro=0, releaselevel="alpha", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo
