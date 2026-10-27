from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_item import CommonItem, CommonItemDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListInboundPlanItemsResponse(SdkBaseModel):
    """The ``listInboundPlanItems`` response., The ``listPackingGroupItems`` response., The ``listShipmentItems``
    response."""

    items: list[CommonItem]
    """The items in an inbound plan."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListInboundPlanItemsResponseDict(TypedDict):
    items: list[CommonItemDict]
    pagination: NotRequired[CommonPaginationDict]
