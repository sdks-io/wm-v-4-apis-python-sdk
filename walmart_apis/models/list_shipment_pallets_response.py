from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .common_pallet import CommonPallet, CommonPalletDict


class ListShipmentPalletsResponse(SdkBaseModel):
    """The ``listShipmentPallets`` response."""

    pallets: list[CommonPallet]
    """The pallets in a shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListShipmentPalletsResponseDict(TypedDict):
    pallets: list[CommonPalletDict]
    pagination: NotRequired[CommonPaginationDict]
