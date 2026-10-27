from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.label_format import LabelFormatOrStr
from .shipment_request_details import ShipmentRequestDetails, ShipmentRequestDetailsDict


class CreateShipmentRequest(SdkBaseModel):
    shipment_request_details: ShipmentRequestDetails = Field(alias="shipmentRequestDetails")
    shipping_service_id: str = Field(alias="shippingServiceId")
    shipping_service_offer_id: Optional[str] = Field(default=UNSET, alias="shippingServiceOfferId")
    label_format: Optional[LabelFormatOrStr] = Field(default=UNSET, alias="labelFormat")


class CreateShipmentRequestDict(TypedDict):
    shipment_request_details: ShipmentRequestDetailsDict
    shipping_service_id: str
    shipping_service_offer_id: NotRequired[str]
    label_format: NotRequired[LabelFormatOrStr]
