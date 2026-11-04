from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type_product_pricing import ConditionTypeProductPricingOrStr
from .enums.customer_type import CustomerTypeOrStr
from .enums.http_method_model import HttpMethodModelOrStr


class ItemOffersRequest(SdkBaseModel):
    """Request parameters for one ``getItemOffers`` operation in the batch."""

    uri: str
    """Resource path of the operation being called in the batch, without query parameters."""

    method: HttpMethodModelOrStr
    """HTTP method used for the individual API request in the batch."""

    headers: Optional[Any] = UNSET
    """Additional HTTP headers to send with an individual batch request."""

    item_condition: ConditionTypeProductPricingOrStr = Field(alias="ItemCondition")
    """Indicates the item condition. Possible values are ``New``, ``Restored``, and ``Pre-Owned``."""

    customer_type: Optional[CustomerTypeOrStr] = Field(default=UNSET, alias="CustomerType")
    """Indicates whether to request ``Consumer`` or ``Business`` offers. The default is ``Consumer``."""

    walmart_item_id: Optional[str] = Field(default=UNSET, alias="walmartItemId")
    """Walmart Item ID that identifies the requested item."""


class ItemOffersRequestDict(TypedDict):
    uri: str
    method: HttpMethodModelOrStr
    headers: NotRequired[Any]
    item_condition: ConditionTypeProductPricingOrStr
    customer_type: NotRequired[CustomerTypeOrStr]
    walmart_item_id: NotRequired[str]
