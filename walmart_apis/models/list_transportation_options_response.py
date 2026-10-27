from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .common_transportation_option import CommonTransportationOption, CommonTransportationOptionDict


class ListTransportationOptionsResponse(SdkBaseModel):
    """The ``listTransportationOptions`` response."""

    transportation_options: list[CommonTransportationOption] = Field(alias="transportationOptions")
    """Transportation options generated for the placement option."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListTransportationOptionsResponseDict(TypedDict):
    transportation_options: list[CommonTransportationOptionDict]
    pagination: NotRequired[CommonPaginationDict]
