from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaginationInventory(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    total_count: Optional[int] = Field(default=UNSET, alias="totalCount")


class PaginationInventoryDict(TypedDict):
    next_token: NotRequired[str]
    total_count: NotRequired[int]
