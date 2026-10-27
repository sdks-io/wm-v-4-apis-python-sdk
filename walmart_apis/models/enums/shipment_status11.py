from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatus11(str, Enum):
    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"

    __str__ = str.__str__


ShipmentStatus11OrStr: TypeAlias = Annotated[ShipmentStatus11 | str, open_enum_validator(ShipmentStatus11)]
