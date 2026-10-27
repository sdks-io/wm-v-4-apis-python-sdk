from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonShipmentSummary(SdkBaseModel):
    """Summary information about a shipment."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of a shipment. A shipment contains the boxes and units being inbounded."""

    status: str
    """The status of a shipment. Possible values: ``ABANDONED``, ``CANCELLED``, ``CHECKED_IN``, ``CLOSED``, ``DELETED``,
    ``DELIVERED``, ``IN_TRANSIT``, ``MIXED``, ``READY_TO_SHIP``, ``RECEIVING``, ``SHIPPED``, ``UNCONFIRMED``,
    ``WORKING``."""


class CommonShipmentSummaryDict(TypedDict):
    shipment_id: str
    status: str
