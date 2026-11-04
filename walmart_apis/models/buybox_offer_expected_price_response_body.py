from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buybox_offer_expected_price_result import BuyboxOfferExpectedPriceResult, BuyboxOfferExpectedPriceResultDict
from .error_catalog_items import ErrorCatalogItems, ErrorCatalogItemsDict
from .offer_identifier import OfferIdentifier, OfferIdentifierDict


class BuyboxOfferExpectedPriceResponseBody(SdkBaseModel):
    """Buybox offer expected price (BOEP) information returned for one offer."""

    offer_identifier: Optional[OfferIdentifier] = Field(default=UNSET, alias="offerIdentifier")
    """Identifies an offer by marketplace, seller, seller SKU, and fulfillment type."""

    buybox_offer_expected_price_results: Optional[list[BuyboxOfferExpectedPriceResult]] = Field(
        default=UNSET, alias="buyboxOfferExpectedPriceResults"
    )
    """BOEP results returned for the requested offer."""

    errors: Optional[list[ErrorCatalogItems]] = UNSET
    """Error responses returned when a request is unsuccessful."""


class BuyboxOfferExpectedPriceResponseBodyDict(TypedDict):
    offer_identifier: NotRequired[OfferIdentifierDict]
    buybox_offer_expected_price_results: NotRequired[list[BuyboxOfferExpectedPriceResultDict]]
    errors: NotRequired[list[ErrorCatalogItemsDict]]
