from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonShipmentSummary(SdkBaseModel):
    """Summary information about a shipment."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of a shipment. A shipment contains the boxes and units being inbounded."""

    status: str
    """The status of a shipment. Possible values: ``PENDING_SHIPMENT_DETAILS``, ``CARRIER_PENDING``,
    ``TRACKING_NEEDED``, ``ISSUES``, ``OUT_FOR_DELIVERY``, ``AWAITING_TRANSIT``, ``IN_TRANSIT``,
    ``TRANSFER_IN_PROGRESS``, ``ARRIVED``, ``RECEIVING``, ``COMPLETED``, ``CANCELLED``, ``CLOSED``, ``UNCONFIRMED``,
    ``PROCESSING``. (aligned with the Inbound Order Workflow upstream vocabulary — -follow-up)"""


class CommonShipmentSummaryDict(TypedDict):
    shipment_id: str
    status: str
