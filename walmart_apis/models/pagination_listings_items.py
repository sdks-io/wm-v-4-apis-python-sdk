from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaginationListingsItems(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    """Cursor for the next page; absent on the last page"""

    previous_token: Optional[str] = Field(default=UNSET, alias="previousToken")
    """Cursor for the previous page; absent on the first page"""


class PaginationListingsItemsDict(TypedDict):
    next_token: NotRequired[str]
    previous_token: NotRequired[str]
