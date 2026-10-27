from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BuyerType(str, Enum):
    B2_B = "B2B"
    B2_C = "B2C"
    ALL = "All"

    __str__ = str.__str__


BuyerTypeOrStr: TypeAlias = Annotated[BuyerType | str, open_enum_validator(BuyerType)]
