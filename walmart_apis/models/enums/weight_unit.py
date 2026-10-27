from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WeightUnit(str, Enum):
    LB = "LB"
    KG = "KG"
    OZ = "OZ"

    __str__ = str.__str__


WeightUnitOrStr: TypeAlias = Annotated[WeightUnit | str, open_enum_validator(WeightUnit)]
