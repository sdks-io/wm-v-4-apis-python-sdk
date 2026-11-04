from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_listings_items import ItemListingsItems, ItemListingsItemsDict
from .pagination_listings_items import PaginationListingsItems, PaginationListingsItemsDict


class ItemSearchResultsListingsItems(SdkBaseModel):
    number_of_results: int = Field(alias="numberOfResults")
    """Total number of matching listings items"""

    pagination: Optional[PaginationListingsItems] = UNSET
    items: list[ItemListingsItems]


class ItemSearchResultsListingsItemsDict(TypedDict):
    number_of_results: int
    pagination: NotRequired[PaginationListingsItemsDict]
    items: list[ItemListingsItemsDict]
