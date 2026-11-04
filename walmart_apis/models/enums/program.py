from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Program(str, Enum):
    """Program for which the item's eligibility is being evaluated."""

    INBOUND = "INBOUND"
    COMMINGLING = "COMMINGLING"

    __str__ = str.__str__


ProgramOrStr: TypeAlias = Annotated[Program | str, open_enum_validator(Program)]
