from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatusOrders(str, Enum):
    """Shipment status to record. For completed deliveries, use the dedicated delivery operation."""

    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"

    __str__ = str.__str__


ShipmentStatusOrdersOrStr: TypeAlias = Annotated[ShipmentStatusOrders | str, open_enum_validator(ShipmentStatusOrders)]
