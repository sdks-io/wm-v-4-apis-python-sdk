from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Status(str, Enum):
    BUYABLE = "BUYABLE"
    SUPPRESSED = "SUPPRESSED"
    DISCOVERABLE = "DISCOVERABLE"

    __str__ = str.__str__


StatusOrStr: TypeAlias = Annotated[Status | str, open_enum_validator(Status)]
