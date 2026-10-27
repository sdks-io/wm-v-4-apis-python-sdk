from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .shipment_request_details import ShipmentRequestDetails, ShipmentRequestDetailsDict


class GetEligibleShippingServicesRequest(SdkBaseModel):
    shipment_request_details: ShipmentRequestDetails = Field(alias="shipmentRequestDetails")


class GetEligibleShippingServicesRequestDict(TypedDict):
    shipment_request_details: ShipmentRequestDetailsDict
