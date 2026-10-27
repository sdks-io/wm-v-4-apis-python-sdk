from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buyer_info import BuyerInfo, BuyerInfoDict


class GetOrderBuyerInfoResponse(SdkBaseModel):
    payload: Optional[BuyerInfo] = UNSET
    """Buyer contact projection. ``buyerPhoneAnonymized`` is masked to the last 4 digits (e.g. ``***-***-0100``); the
    unmasked phone number is never returned by the v4 API."""


class GetOrderBuyerInfoResponseDict(TypedDict):
    payload: NotRequired[BuyerInfoDict]
