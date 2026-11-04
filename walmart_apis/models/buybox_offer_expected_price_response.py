from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .buybox_offer_expected_price_response_body import (
    BuyboxOfferExpectedPriceResponseBody,
    BuyboxOfferExpectedPriceResponseBodyDict,
)
from .get_offers_http_status_line import GetOffersHttpStatusLine, GetOffersHttpStatusLineDict


class BuyboxOfferExpectedPriceResponse(SdkBaseModel):
    """Buybox offer expected price (BOEP) response for one request in the batch."""

    status: Optional[GetOffersHttpStatusLine] = UNSET
    """HTTP status information associated with the response."""

    body: Optional[BuyboxOfferExpectedPriceResponseBody] = UNSET
    """Buybox offer expected price (BOEP) information returned for one offer."""


class BuyboxOfferExpectedPriceResponseDict(TypedDict):
    status: NotRequired[GetOffersHttpStatusLineDict]
    body: NotRequired[BuyboxOfferExpectedPriceResponseBodyDict]
