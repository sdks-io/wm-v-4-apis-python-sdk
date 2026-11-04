from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Program1(str, Enum):
    INBOUND = "INBOUND"
    COMMINGLING = "COMMINGLING"

    __str__ = str.__str__


Program1OrStr: TypeAlias = Annotated[Program1 | str, open_enum_validator(Program1)]
