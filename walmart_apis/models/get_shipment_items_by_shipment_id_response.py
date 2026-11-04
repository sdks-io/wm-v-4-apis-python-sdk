from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .shipment_item_by_shipment_id import ShipmentItemByShipmentId, ShipmentItemByShipmentIdDict


class GetShipmentItemsByShipmentIdResponse(SdkBaseModel):
    """The ``getShipmentItemsByShipmentId`` response . ``pagination.nextToken`` is sourced directly from upstream
    Inbound Order Workflow's ``NextToken`` field (unlike most other list operations in this API, which already use a
    lowercase ``nextToken`` upstream) -- pass it back as the ``paginationToken`` query parameter to fetch the next
    page."""

    items: list[ShipmentItemByShipmentId]
    """The items in the confirmed shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class GetShipmentItemsByShipmentIdResponseDict(TypedDict):
    items: list[ShipmentItemByShipmentIdDict]
    pagination: NotRequired[CommonPaginationDict]
