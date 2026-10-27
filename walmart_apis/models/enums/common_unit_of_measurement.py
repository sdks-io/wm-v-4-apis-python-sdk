from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonUnitOfMeasurement(str, Enum):
    """Unit of linear measure."""

    IN = "IN"
    CM = "CM"

    __str__ = str.__str__


CommonUnitOfMeasurementOrStr: TypeAlias = Annotated[
    CommonUnitOfMeasurement | str, open_enum_validator(CommonUnitOfMeasurement)
]
