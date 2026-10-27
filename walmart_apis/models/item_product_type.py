from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemProductType(SdkBaseModel):
    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    """Walmart product type (e.g. "Electronics", "Clothing")"""


class ItemProductTypeDict(TypedDict):
    product_type: NotRequired[str]
