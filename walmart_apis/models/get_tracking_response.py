from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload1_shipping import Payload1Shipping, Payload1ShippingDict


class GetTrackingResponse(SdkBaseModel):
    payload: Optional[Payload1Shipping] = UNSET


class GetTrackingResponseDict(TypedDict):
    payload: NotRequired[Payload1ShippingDict]
