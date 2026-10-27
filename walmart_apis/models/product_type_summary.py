from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductTypeSummary(SdkBaseModel):
    name: Optional[str] = UNSET
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    marketplace_ids: Optional[list[str]] = Field(default=UNSET, alias="marketplaceIds")


class ProductTypeSummaryDict(TypedDict):
    name: NotRequired[str]
    display_name: NotRequired[str]
    marketplace_ids: NotRequired[list[str]]
