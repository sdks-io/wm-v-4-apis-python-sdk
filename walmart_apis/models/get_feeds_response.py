from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .feed import Feed, FeedDict


class GetFeedsResponse(SdkBaseModel):
    feeds: Optional[list[Feed]] = UNSET
    """List of feeds matching the request filters"""

    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    """Token to retrieve the next page of results; absent when no more pages exist"""


class GetFeedsResponseDict(TypedDict):
    feeds: NotRequired[list[FeedDict]]
    next_token: NotRequired[str]
