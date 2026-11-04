from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentStatus(str, Enum):
    """The status of a shipment, as returned by ``getShipments`` (upstream ``ShipmentStatusList`` /
    ``ShipmentData.ShipmentStatus``). A hard enum here is safe -- this is a net-new v4 response shape with no
    pre-existing consumers, unlike the free-string ``Shipment.status`` field on the ``getShipment`` sibling op (which
    carries the same vocabulary PLUS ``UNCONFIRMED``, kept as a free string there for that op's own historical
    reasons)."""

    PENDING_SHIPMENT_DETAILS = "PENDING_SHIPMENT_DETAILS"
    CARRIER_PENDING = "CARRIER_PENDING"
    TRACKING_NEEDED = "TRACKING_NEEDED"
    ISSUES = "ISSUES"
    OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
    AWAITING_TRANSIT = "AWAITING_TRANSIT"
    IN_TRANSIT = "IN_TRANSIT"
    TRANSFER_IN_PROGRESS = "TRANSFER_IN_PROGRESS"
    ARRIVED = "ARRIVED"
    RECEIVING = "RECEIVING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    CLOSED = "CLOSED"
    PROCESSING = "PROCESSING"

    __str__ = str.__str__


ShipmentStatusOrStr: TypeAlias = Annotated[ShipmentStatus | str, open_enum_validator(ShipmentStatus)]
