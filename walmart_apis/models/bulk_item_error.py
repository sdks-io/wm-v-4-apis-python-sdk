from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BulkItemError(SdkBaseModel):
    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")
    code: Optional[str] = UNSET
    message: Optional[str] = UNSET


class BulkItemErrorDict(TypedDict):
    seller_sku: NotRequired[str]
    code: NotRequired[str]
    message: NotRequired[str]
