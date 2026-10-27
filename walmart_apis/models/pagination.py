from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pagination(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    previous_token: Optional[str] = Field(default=UNSET, alias="previousToken")


class PaginationDict(TypedDict):
    next_token: NotRequired[str]
    previous_token: NotRequired[str]
