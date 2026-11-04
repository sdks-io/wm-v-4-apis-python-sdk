from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload3 import Payload3, Payload3Dict


class CancelShipmentResponseShipping(SdkBaseModel):
    payload: Optional[Payload3] = UNSET


class CancelShipmentResponseShippingDict(TypedDict):
    payload: NotRequired[Payload3Dict]
