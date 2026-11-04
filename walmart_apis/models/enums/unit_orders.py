from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class UnitOrders(str, Enum):
    """Unit of measure for the quantity."""

    EA = "EA"
    EACH = "EACH"
    CASE = "CASE"
    CARTON = "CARTON"

    __str__ = str.__str__


UnitOrdersOrStr: TypeAlias = Annotated[UnitOrders | str, open_enum_validator(UnitOrders)]
