from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.shipment_status1 import ShipmentStatus1OrStr
from .update_shipment_status_line import UpdateShipmentStatusLine, UpdateShipmentStatusLineDict


class UpdateShipmentStatusRequest(SdkBaseModel):
    shipment_status: ShipmentStatus1OrStr = Field(alias="shipmentStatus")
    """Non-terminal shipment-lifecycle state. Mirrors Amazon SP-API Orders v0 ``shipmentStatus``. For terminal
    ``Delivered`` use the dedicated ``/deliver`` endpoint."""

    status_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusDate")
    """ISO-8601 timestamp at which the seller observed the status change. Optional — if omitted, FMS defaults to server
    time."""

    order_lines: list[UpdateShipmentStatusLine] = Field(alias="orderLines")


class UpdateShipmentStatusRequestDict(TypedDict):
    shipment_status: ShipmentStatus1OrStr
    status_date: NotRequired[RFC3339DateTime]
    order_lines: list[UpdateShipmentStatusLineDict]
