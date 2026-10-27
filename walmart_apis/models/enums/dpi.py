from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Dpi(int, Enum):
    VALUE_203 = 203
    VALUE_300 = 300

    __str__ = str.__str__


DpiOrInt: TypeAlias = Annotated[Dpi | int, open_enum_validator(Dpi)]
