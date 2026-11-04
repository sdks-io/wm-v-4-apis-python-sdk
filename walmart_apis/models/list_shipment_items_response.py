from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_item import CommonItem, CommonItemDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListShipmentItemsResponse(SdkBaseModel):
    """The ``listShipmentItems`` response."""

    items: list[CommonItem]
    """The items in a shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListShipmentItemsResponseDict(TypedDict):
    items: list[CommonItemDict]
    pagination: NotRequired[CommonPaginationDict]
