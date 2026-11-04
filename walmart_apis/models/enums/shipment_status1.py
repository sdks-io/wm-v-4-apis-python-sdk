from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatus1(str, Enum):
    """Shipment status recorded for the specified order lines."""

    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"

    __str__ = str.__str__


ShipmentStatus1OrStr: TypeAlias = Annotated[ShipmentStatus1 | str, open_enum_validator(ShipmentStatus1)]
