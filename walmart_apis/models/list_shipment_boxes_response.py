from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_box import CommonBox, CommonBoxDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListShipmentBoxesResponse(SdkBaseModel):
    """The ``listShipmentBoxes`` response."""

    boxes: list[CommonBox]
    """A list of boxes in a shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListShipmentBoxesResponseDict(TypedDict):
    boxes: list[CommonBoxDict]
    pagination: NotRequired[CommonPaginationDict]
