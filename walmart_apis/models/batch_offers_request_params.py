from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type_product_pricing import ConditionTypeProductPricingOrStr
from .enums.customer_type import CustomerTypeOrStr


class BatchOffersRequestParams(SdkBaseModel):
    """Common request parameters for ``ItemOffersRequest`` and ``ListingOffersRequest``. Does not carry a MarketplaceId
    -- the marketplace is resolved from the gateway-derived tenant context (x-o-tenant), same as every other pricing
    endpoint. See PricingValidation#currentMarketplaceId."""

    item_condition: ConditionTypeProductPricingOrStr = Field(alias="ItemCondition")
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    customer_type: Optional[CustomerTypeOrStr] = Field(default=UNSET, alias="CustomerType")
    """Indicates whether to request ``Consumer`` or ``Business`` offers. The default is ``Consumer``."""


class BatchOffersRequestParamsDict(TypedDict):
    item_condition: ConditionTypeProductPricingOrStr
    customer_type: NotRequired[CustomerTypeOrStr]
