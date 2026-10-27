from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pagination1(SdkBaseModel):
    pagination_token: Optional[str] = Field(default=UNSET, alias="paginationToken")


class Pagination1Dict(TypedDict):
    pagination_token: NotRequired[str]
