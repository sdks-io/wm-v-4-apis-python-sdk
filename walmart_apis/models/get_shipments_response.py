from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .shipment_summary import ShipmentSummary, ShipmentSummaryDict


class GetShipmentsResponse(SdkBaseModel):
    """The ``getShipments`` response."""

    shipments: list[ShipmentSummary]
    """Shipments matching the requested filters."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class GetShipmentsResponseDict(TypedDict):
    shipments: list[ShipmentSummaryDict]
    pagination: NotRequired[CommonPaginationDict]
