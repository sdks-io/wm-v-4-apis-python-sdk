from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_packing_option import CommonPackingOption, CommonPackingOptionDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListPackingOptionsResponse(SdkBaseModel):
    """The ``listPackingOptions`` response."""

    packing_options: list[CommonPackingOption] = Field(alias="packingOptions")
    """List of packing options."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListPackingOptionsResponseDict(TypedDict):
    packing_options: list[CommonPackingOptionDict]
    pagination: NotRequired[CommonPaginationDict]
