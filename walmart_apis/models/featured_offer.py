from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type import MoneyType, MoneyTypeDict
from .offer_identifier import OfferIdentifier, OfferIdentifierDict


class FeaturedOffer(SdkBaseModel):
    """A featured offer."""

    offer_identifier: Optional[OfferIdentifier] = Field(default=UNSET, alias="offerIdentifier")
    """Identifies an offer."""

    condition: Optional[str] = UNSET
    """The item condition."""

    price: Optional[MoneyType] = UNSET
    """Currency type and monetary value."""


class FeaturedOfferDict(TypedDict):
    offer_identifier: NotRequired[OfferIdentifierDict]
    condition: NotRequired[str]
    price: NotRequired[MoneyTypeDict]
