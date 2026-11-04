from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .common_pallet import CommonPallet, CommonPalletDict


class ListInboundPlanPalletsResponse(SdkBaseModel):
    """Paginated response containing pallets in an inbound plan."""

    pallets: list[CommonPallet]
    """Pallets included in the inbound plan."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListInboundPlanPalletsResponseDict(TypedDict):
    pallets: list[CommonPalletDict]
    pagination: NotRequired[CommonPaginationDict]
