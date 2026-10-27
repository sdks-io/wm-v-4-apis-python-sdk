from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.condition_type2 import ConditionType2OrStr
from .enums.customer_type import CustomerTypeOrStr
from .enums.http_method_model import HttpMethodModelOrStr


class ListingOffersRequest(SdkBaseModel):
    """List of request parameters accepted by the getListingOffers operation."""

    uri: str
    """The resource path of the operation being called in batch, without query parameters."""

    method: HttpMethodModelOrStr
    """The HTTP method associated with the individual APIs being called as part of the batch request."""

    headers: Optional[Any] = UNSET
    """A mapping of additional HTTP headers to send for the individual batch request."""

    marketplace_id: str = Field(alias="MarketplaceId")
    """A marketplace identifier."""

    item_condition: ConditionType2OrStr = Field(alias="ItemCondition")
    """Indicates the condition of the item. Possible values: New, Used, Collectible, Refurbished, Club."""

    customer_type: Optional[CustomerTypeOrStr] = Field(default=UNSET, alias="CustomerType")
    """Indicates whether to request Consumer or Business offers. Default is Consumer."""

    seller_sku: str = Field(alias="SellerSKU")
    """The seller stock keeping unit (SKU) of the item."""


class ListingOffersRequestDict(TypedDict):
    uri: str
    method: HttpMethodModelOrStr
    headers: NotRequired[Any]
    marketplace_id: str
    item_condition: ConditionType2OrStr
    customer_type: NotRequired[CustomerTypeOrStr]
    seller_sku: str
