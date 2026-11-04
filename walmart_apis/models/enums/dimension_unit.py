from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class DimensionUnit(str, Enum):
    """Unit used for package length, width, and height. Default: ``IN``."""

    IN = "IN"
    CM = "CM"

    __str__ = str.__str__


DimensionUnitOrStr: TypeAlias = Annotated[DimensionUnit | str, open_enum_validator(DimensionUnit)]
