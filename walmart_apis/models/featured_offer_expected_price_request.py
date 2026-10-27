from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FeaturedOfferExpectedPriceRequest(SdkBaseModel):
    """An individual FOEP request for a particular SKU."""

    marketplace_id: str = Field(alias="marketplaceId")
    """A marketplace identifier."""

    sku: str
    """The seller stock keeping unit (SKU) of the item."""


class FeaturedOfferExpectedPriceRequestDict(TypedDict):
    marketplace_id: str
    sku: str
