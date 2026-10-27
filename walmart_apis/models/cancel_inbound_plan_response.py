from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelInboundPlanResponse(SdkBaseModel):
    """The ``cancelInboundPlan`` response., The ``generateDeliveryWindowOptions`` response., The
    ``confirmDeliveryWindowOptions`` response., The ``cancelSelfShipAppointment`` response., The
    ``generateSelfShipAppointmentSlots`` response., The ``setPackingInformation`` response., The
    ``generatePackingOptions`` response., The ``confirmPackingOption`` response., The ``generatePlacementOptions``
    response., The ``confirmPlacementOption`` response., The ``generateTransportationOptions`` response., The
    ``confirmTransportationOptions`` response., The ``updateItemComplianceDetails`` response., The ``setPrepDetails``
    response., The ``updateShipmentSourceAddress`` response., The ``updateShipmentTrackingDetails`` response., The
    ``generateShipmentContentUpdatePreviews`` response., The ``confirmShipmentContentUpdatePreview`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class CancelInboundPlanResponseDict(TypedDict):
    operation_id: str
