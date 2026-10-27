from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload import Payload, PayloadDict


class GetFulfillmentOrderResponse(SdkBaseModel):
    payload: Optional[Payload] = UNSET


class GetFulfillmentOrderResponseDict(TypedDict):
    payload: NotRequired[PayloadDict]
