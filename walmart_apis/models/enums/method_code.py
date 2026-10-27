from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MethodCode(str, Enum):
    STANDARD = "Standard"
    EXPRESS = "Express"
    SAME_DAY = "SameDay"
    FREIGHT = "Freight"

    __str__ = str.__str__


MethodCodeOrStr: TypeAlias = Annotated[MethodCode | str, open_enum_validator(MethodCode)]
