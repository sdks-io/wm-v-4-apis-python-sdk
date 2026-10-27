from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SalesRank(SdkBaseModel):
    category_id: Optional[str] = Field(default=UNSET, alias="categoryId")
    rank: Optional[int] = UNSET
    category_name: Optional[str] = Field(default=UNSET, alias="categoryName")
    link: Optional[str] = UNSET


class SalesRankDict(TypedDict):
    category_id: NotRequired[str]
    rank: NotRequired[int]
    category_name: NotRequired[str]
    link: NotRequired[str]
