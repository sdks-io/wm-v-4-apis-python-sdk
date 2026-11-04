from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_box import CommonBox, CommonBoxDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListInboundPlanBoxesResponse(SdkBaseModel):
    """Paginated response containing boxes in an inbound plan."""

    boxes: list[CommonBox]
    """Shipping boxes included in the inbound plan."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListInboundPlanBoxesResponseDict(TypedDict):
    boxes: list[CommonBoxDict]
    pagination: NotRequired[CommonPaginationDict]
