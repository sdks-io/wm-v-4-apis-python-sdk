from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buybox_offer_expected_price_request import BuyboxOfferExpectedPriceRequest, BuyboxOfferExpectedPriceRequestDict


class GetBuyboxOfferExpectedPriceBatchRequest(SdkBaseModel):
    """Request body for the ``getBuyboxOfferExpectedPriceBatch`` operation."""

    requests: Optional[list[BuyboxOfferExpectedPriceRequest]] = UNSET
    """Buybox offer expected price (BOEP) requests to process in the batch."""


class GetBuyboxOfferExpectedPriceBatchRequestDict(TypedDict):
    requests: NotRequired[list[BuyboxOfferExpectedPriceRequestDict]]
