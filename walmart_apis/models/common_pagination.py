from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonPagination(SdkBaseModel):
    """Contains tokens to fetch from a certain page."""

    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    """When present, pass this string token in the next request to return the next response page."""


class CommonPaginationDict(TypedDict):
    next_token: NotRequired[str]
