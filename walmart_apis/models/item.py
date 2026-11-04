from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict
from .item_image import ItemImage, ItemImageDict
from .item_product_type import ItemProductType, ItemProductTypeDict
from .item_relationship import ItemRelationship, ItemRelationshipDict
from .sales_rank import SalesRank, SalesRankDict


class Item(SdkBaseModel):
    """Catalog information for an item in the specified marketplace."""

    walmart_item_id: str = Field(alias="walmartItemId")
    """Walmart catalog item identifier. Confirm whether this is a 14-digit Walmart Item ID or an alphanumeric Walmart
    Product ID (WPID)."""

    marketplace_id: str = Field(alias="marketplaceId")
    """Walmart Marketplace identifier associated with the item."""

    attributes: Optional[dict[str, Any]] = UNSET
    """Product attributes, such as name, brand, and description."""

    identifiers: Optional[ItemIdentifiers] = UNSET
    """Walmart item identifiers and seller SKU identifiers associated with the item."""

    images: Optional[list[ItemImage]] = UNSET
    product_types: Optional[list[ItemProductType]] = Field(default=UNSET, alias="productTypes")
    sales_ranks: Optional[list[SalesRank]] = Field(default=UNSET, alias="salesRanks")
    relationships: Optional[list[ItemRelationship]] = UNSET
    """Relationships between this catalog item and related catalog items."""

    variant_count: OptionalNullable[int] = Field(default=UNSET, alias="variantCount")
    """Number of items in the variant group, when available."""


class ItemDict(TypedDict):
    walmart_item_id: str
    marketplace_id: str
    attributes: NotRequired[dict[str, Any]]
    identifiers: NotRequired[ItemIdentifiersDict]
    images: NotRequired[list[ItemImageDict]]
    product_types: NotRequired[list[ItemProductTypeDict]]
    sales_ranks: NotRequired[list[SalesRankDict]]
    relationships: NotRequired[list[ItemRelationshipDict]]
    variant_count: NotRequired[int | None]
