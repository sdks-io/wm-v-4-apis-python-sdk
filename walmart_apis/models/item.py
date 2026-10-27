from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_identifiers import ItemIdentifiers, ItemIdentifiersDict
from .item_image import ItemImage, ItemImageDict
from .item_product_type import ItemProductType, ItemProductTypeDict
from .item_relationship import ItemRelationship, ItemRelationshipDict
from .sales_rank import SalesRank, SalesRankDict


class Item(SdkBaseModel):
    walmart_item_id: str = Field(alias="walmartItemId")
    """Walmart Product ID (WPID) — alphanumeric catalog identifier"""

    marketplace_id: str = Field(alias="marketplaceId")
    attributes: Optional[dict[str, Any]] = UNSET
    """Key product attributes (name, brand, description, etc.)"""

    identifiers: Optional[ItemIdentifiers] = UNSET
    images: Optional[list[ItemImage]] = UNSET
    product_types: Optional[list[ItemProductType]] = Field(default=UNSET, alias="productTypes")
    sales_ranks: Optional[list[SalesRank]] = Field(default=UNSET, alias="salesRanks")
    relationships: Optional[list[ItemRelationship]] = UNSET
    """Variant relationships (e.g. color/size variants)"""


class ItemDict(TypedDict):
    walmart_item_id: str
    marketplace_id: str
    attributes: NotRequired[dict[str, Any]]
    identifiers: NotRequired[ItemIdentifiersDict]
    images: NotRequired[list[ItemImageDict]]
    product_types: NotRequired[list[ItemProductTypeDict]]
    sales_ranks: NotRequired[list[SalesRankDict]]
    relationships: NotRequired[list[ItemRelationshipDict]]
