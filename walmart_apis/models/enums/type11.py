from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class Type11(str, Enum):
    PICKUP = "PICKUP"
    DROPOFF = "DROPOFF"

    __str__ = str.__str__


Type11OrStr: TypeAlias = Annotated[Type11 | str, open_enum_validator(Type11)]
