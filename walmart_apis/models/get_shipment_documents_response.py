from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload2_shipping import Payload2Shipping, Payload2ShippingDict


class GetShipmentDocumentsResponse(SdkBaseModel):
    payload: Optional[Payload2Shipping] = UNSET


class GetShipmentDocumentsResponseDict(TypedDict):
    payload: NotRequired[Payload2ShippingDict]
