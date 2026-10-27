from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pagination3(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")


class Pagination3Dict(TypedDict):
    next_token: NotRequired[str]
