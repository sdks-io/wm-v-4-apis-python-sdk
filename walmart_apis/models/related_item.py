from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RelatedItem(SdkBaseModel):
    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")


class RelatedItemDict(TypedDict):
    walmart_item_id: NotRequired[str]
