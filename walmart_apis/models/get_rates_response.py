from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload_shipping import PayloadShipping, PayloadShippingDict


class GetRatesResponse(SdkBaseModel):
    payload: Optional[PayloadShipping] = UNSET


class GetRatesResponseDict(TypedDict):
    payload: NotRequired[PayloadShippingDict]
