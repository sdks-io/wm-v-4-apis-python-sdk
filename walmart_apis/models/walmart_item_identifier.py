from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WalmartItemIdentifier(SdkBaseModel):
    """Walmart Marketplace and Walmart Item ID that identify the item."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """Walmart Marketplace identifier associated with the item."""

    walmart_item_id: str = Field(alias="walmartItemId")
    """Walmart Item ID that identifies the item."""


class WalmartItemIdentifierDict(TypedDict):
    marketplace_id: str
    walmart_item_id: str
