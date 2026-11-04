from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemProductType(SdkBaseModel):
    """Product type assigned to the catalog item."""

    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """Walmart product type, such as Electronics or Clothing."""


class ItemProductTypeDict(TypedDict):
    product_type: NotRequired[str]
