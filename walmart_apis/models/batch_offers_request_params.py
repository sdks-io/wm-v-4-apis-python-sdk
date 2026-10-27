from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type2 import ConditionType2OrStr
from .enums.customer_type import CustomerTypeOrStr


class BatchOffersRequestParams(SdkBaseModel):
    """Common request parameters for ItemOffersRequest and ListingOffersRequest."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """A marketplace identifier."""

    item_condition: ConditionType2OrStr = Field(alias="ItemCondition")
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""

    customer_type: Optional[CustomerTypeOrStr] = Field(default=UNSET, alias="CustomerType")
    """Indicates whether to request Consumer or Business offers. Default is Consumer."""


class BatchOffersRequestParamsDict(TypedDict):
    marketplace_id: str
    item_condition: ConditionType2OrStr
    customer_type: NotRequired[CustomerTypeOrStr]
