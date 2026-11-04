from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .purchase_shipment_response_payload import PurchaseShipmentResponsePayload, PurchaseShipmentResponsePayloadDict


class PurchaseShipmentResponse(SdkBaseModel):
    payload: Optional[PurchaseShipmentResponsePayload] = UNSET


class PurchaseShipmentResponseDict(TypedDict):
    payload: NotRequired[PurchaseShipmentResponsePayloadDict]
