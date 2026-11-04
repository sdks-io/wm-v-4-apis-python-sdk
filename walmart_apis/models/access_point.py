from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_merchant_fulfillment_seller_fulfilled_labels import (
    AddressMerchantFulfillmentSellerFulfilledLabels,
    AddressMerchantFulfillmentSellerFulfilledLabelsDict,
)
from .enums.type1 import Type1OrStr


class AccessPoint(SdkBaseModel):
    access_point_id: str = Field(alias="accessPointId")
    name: str
    type_: Optional[Type1OrStr] = Field(default=UNSET, alias="type")
    address: AddressMerchantFulfillmentSellerFulfilledLabels
    operating_hours: Optional[Any] = Field(default=UNSET, alias="operatingHours")
    """Per-day operating hours. Compressed shape; full DayOfWeekTimeMap fidelity tracked in a follow-up PR."""

    timezone: Optional[str] = UNSET
    """IANA timezone name (e.g. America/Los_Angeles)."""


class AccessPointDict(TypedDict):
    access_point_id: str
    name: str
    type_: NotRequired[Type1OrStr]
    address: AddressMerchantFulfillmentSellerFulfilledLabelsDict
    operating_hours: NotRequired[Any]
    timezone: NotRequired[str]
