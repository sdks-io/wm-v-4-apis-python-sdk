from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WalmartItemIdentifier(SdkBaseModel):
    """Schema to identify an item by MarketPlaceId and Walmart Item ID ."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """A marketplace identifier."""

    walmart_item_id: str = Field(alias="walmartItemId")
    """The Walmart Item ID of the item."""


class WalmartItemIdentifierDict(TypedDict):
    marketplace_id: str
    walmart_item_id: str
