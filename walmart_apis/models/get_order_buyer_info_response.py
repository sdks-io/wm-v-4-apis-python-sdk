from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buyer_info import BuyerInfo, BuyerInfoDict


class GetOrderBuyerInfoResponse(SdkBaseModel):
    """Response containing the requested order's buyer information."""

    payload: Optional[BuyerInfo] = UNSET
    """Buyer name, email address, and anonymized phone number."""


class GetOrderBuyerInfoResponseDict(TypedDict):
    payload: NotRequired[BuyerInfoDict]
