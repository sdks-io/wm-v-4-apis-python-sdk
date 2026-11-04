from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buybox_offer import BuyboxOffer, BuyboxOfferDict
from .buybox_offer_expected_price import BuyboxOfferExpectedPrice, BuyboxOfferExpectedPriceDict


class BuyboxOfferExpectedPriceResult(SdkBaseModel):
    """Buybox offer expected price result for a specific offer."""

    buybox_offer_expected_price: Optional[BuyboxOfferExpectedPrice] = Field(
        default=UNSET, alias="buyboxOfferExpectedPrice"
    )
    """Buybox offer expected price for a seller SKU."""

    result_status: Optional[str] = Field(default=UNSET, alias="resultStatus")
    """Status of the buybox offer expected price (BOEP) request."""

    competing_buybox_offer: Optional[BuyboxOffer] = Field(default=UNSET, alias="competingBuyboxOffer")
    """Buybox offer information, including the offer identifier, item condition, and price."""

    current_buybox_offer: Optional[BuyboxOffer] = Field(default=UNSET, alias="currentBuyboxOffer")
    """Buybox offer information, including the offer identifier, item condition, and price."""


class BuyboxOfferExpectedPriceResultDict(TypedDict):
    buybox_offer_expected_price: NotRequired[BuyboxOfferExpectedPriceDict]
    result_status: NotRequired[str]
    competing_buybox_offer: NotRequired[BuyboxOfferDict]
    current_buybox_offer: NotRequired[BuyboxOfferDict]
