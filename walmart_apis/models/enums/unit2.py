from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Unit2(str, Enum):
    EA = "EA"
    EACH = "EACH"
    CASE = "CASE"
    CARTON = "CARTON"

    __str__ = str.__str__


Unit2OrStr: TypeAlias = Annotated[Unit2 | str, open_enum_validator(Unit2)]
