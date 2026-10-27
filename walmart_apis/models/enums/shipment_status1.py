from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatus1(str, Enum):
    """Non-terminal shipment-lifecycle state. Mirrors Amazon SP-API Orders v0 ``shipmentStatus``. For terminal
    ``Delivered`` use the dedicated ``/deliver`` endpoint."""

    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"

    __str__ = str.__str__


ShipmentStatus1OrStr: TypeAlias = Annotated[ShipmentStatus1 | str, open_enum_validator(ShipmentStatus1)]
