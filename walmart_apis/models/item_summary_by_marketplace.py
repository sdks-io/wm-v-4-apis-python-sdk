from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.condition_type import ConditionTypeOrStr
from .enums.status import StatusOrStr
from .item_image1 import ItemImage1, ItemImage1Dict


class ItemSummaryByMarketplace(SdkBaseModel):
    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    product_type: Optional[str] = Field(default=UNSET, alias="productType")
    condition_type: Optional[ConditionTypeOrStr] = Field(default=UNSET, alias="conditionType")
    status: Optional[StatusOrStr] = UNSET
    item_name: Optional[str] = Field(default=UNSET, alias="itemName")
    created_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdDate")
    last_updated_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdatedDate")
    main_image: Optional[ItemImage1] = Field(default=UNSET, alias="mainImage")


class ItemSummaryByMarketplaceDict(TypedDict):
    marketplace_id: NotRequired[str]
    walmart_item_id: NotRequired[str]
    product_type: NotRequired[str]
    condition_type: NotRequired[ConditionTypeOrStr]
    status: NotRequired[StatusOrStr]
    item_name: NotRequired[str]
    created_date: NotRequired[RFC3339DateTime]
    last_updated_date: NotRequired[RFC3339DateTime]
    main_image: NotRequired[ItemImage1Dict]
