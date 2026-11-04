from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_item import CommonItem, CommonItemDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListPackingGroupItemsResponse(SdkBaseModel):
    """The ``listPackingGroupItems`` response."""

    items: list[CommonItem]
    """A list of items in the packing group."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListPackingGroupItemsResponseDict(TypedDict):
    items: list[CommonItemDict]
    pagination: NotRequired[CommonPaginationDict]
