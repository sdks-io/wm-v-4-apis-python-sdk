from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buybox_offer_expected_price_response import BuyboxOfferExpectedPriceResponse, BuyboxOfferExpectedPriceResponseDict


class GetBuyboxOfferExpectedPriceBatchResponse(SdkBaseModel):
    """Response schema for the ``getBuyboxOfferExpectedPriceBatch`` operation."""

    responses: Optional[list[BuyboxOfferExpectedPriceResponse]] = UNSET
    """Buybox offer expected price (BOEP) responses returned for the batch."""


class GetBuyboxOfferExpectedPriceBatchResponseDict(TypedDict):
    responses: NotRequired[list[BuyboxOfferExpectedPriceResponseDict]]
