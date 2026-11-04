from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict
from .offer_identifier import OfferIdentifier, OfferIdentifierDict


class BuyboxOffer(SdkBaseModel):
    """Buybox offer information, including the offer identifier, item condition, and price."""

    offer_identifier: Optional[OfferIdentifier] = Field(default=UNSET, alias="offerIdentifier")
    """Identifies an offer by marketplace, seller, seller SKU, and fulfillment type."""

    condition: Optional[str] = UNSET
    """Item condition for the buybox offer."""

    price: Optional[MoneyType] = UNSET
    """Currency type and monetary value."""


class BuyboxOfferDict(TypedDict):
    offer_identifier: NotRequired[OfferIdentifierDict]
    condition: NotRequired[str]
    price: NotRequired[MoneyTypeDict]
