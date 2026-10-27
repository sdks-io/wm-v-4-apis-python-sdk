from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class UpdateInventoryResponse(SdkBaseModel):
    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")
    quantity: Optional[int] = UNSET
    """Echoed from request — plain integer, unit always EA."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")


class UpdateInventoryResponseDict(TypedDict):
    seller_sku: NotRequired[str]
    quantity: NotRequired[int]
    updated_at: NotRequired[RFC3339DateTime]
