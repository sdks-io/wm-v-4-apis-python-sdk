from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.shipment_status_orders import ShipmentStatusOrdersOrStr
from .update_shipment_status_line import UpdateShipmentStatusLine, UpdateShipmentStatusLineDict


class UpdateShipmentStatusRequest(SdkBaseModel):
    """Request to record shipment status for specified order lines."""

    shipment_status: ShipmentStatusOrdersOrStr = Field(alias="shipmentStatus")
    """Shipment status to record. For completed deliveries, use the dedicated delivery operation."""

    status_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusDate")
    """Date and time when the shipment status changed, in ISO 8601 format. If omitted, the service uses its current
    time."""

    order_lines: list[UpdateShipmentStatusLine] = Field(alias="orderLines")


class UpdateShipmentStatusRequestDict(TypedDict):
    shipment_status: ShipmentStatusOrdersOrStr
    status_date: NotRequired[RFC3339DateTime]
    order_lines: list[UpdateShipmentStatusLineDict]
