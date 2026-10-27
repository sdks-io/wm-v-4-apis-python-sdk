from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload1 import Payload1, Payload1Dict


class GetFulfillmentOrderShipmentsResponse(SdkBaseModel):
    payload: Optional[Payload1] = UNSET


class GetFulfillmentOrderShipmentsResponseDict(TypedDict):
    payload: NotRequired[Payload1Dict]
