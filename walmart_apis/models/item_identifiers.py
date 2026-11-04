from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_identifier import ItemIdentifier, ItemIdentifierDict


class ItemIdentifiers(SdkBaseModel):
    """Walmart item identifiers and seller SKU identifiers associated with the item."""

    marketplace_walmart_item_id: Optional[list[ItemIdentifier]] = Field(default=UNSET, alias="marketplaceWalmartItemId")
    sku_identifiers: Optional[list[ItemIdentifier]] = Field(default=UNSET, alias="skuIdentifiers")


class ItemIdentifiersDict(TypedDict):
    marketplace_walmart_item_id: NotRequired[list[ItemIdentifierDict]]
    sku_identifiers: NotRequired[list[ItemIdentifierDict]]
