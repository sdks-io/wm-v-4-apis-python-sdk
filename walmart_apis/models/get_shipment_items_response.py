from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .shipment_item import ShipmentItem, ShipmentItemDict


class GetShipmentItemsResponse(SdkBaseModel):
    """The ``getShipmentItems`` response."""

    items: list[ShipmentItem]
    """Shipment items matching the requested date-range filter."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class GetShipmentItemsResponseDict(TypedDict):
    items: list[ShipmentItemDict]
    pagination: NotRequired[CommonPaginationDict]
