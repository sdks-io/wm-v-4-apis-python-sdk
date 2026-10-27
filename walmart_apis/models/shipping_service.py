from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.carrier_name import CarrierNameOrStr
from .money import Money, MoneyDict
from .shipping_service_options import ShippingServiceOptions, ShippingServiceOptionsDict


class ShippingService(SdkBaseModel):
    shipping_service_id: str = Field(alias="shippingServiceId")
    carrier_name: CarrierNameOrStr = Field(alias="carrierName")
    shipping_service_name: Optional[str] = Field(default=UNSET, alias="shippingServiceName")
    shipping_service_offer_id: str = Field(alias="shippingServiceOfferId")
    ship_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shipDate")
    earliest_estimated_delivery_date: Optional[RFC3339DateTime] = Field(
        default=UNSET, alias="earliestEstimatedDeliveryDate"
    )
    latest_estimated_delivery_date: Optional[RFC3339DateTime] = Field(
        default=UNSET, alias="latestEstimatedDeliveryDate"
    )
    rate: Optional[Money] = UNSET
    shipping_service_options: Optional[ShippingServiceOptions] = Field(default=UNSET, alias="shippingServiceOptions")


class ShippingServiceDict(TypedDict):
    shipping_service_id: str
    carrier_name: CarrierNameOrStr
    shipping_service_name: NotRequired[str]
    shipping_service_offer_id: str
    ship_date: NotRequired[RFC3339DateTime]
    earliest_estimated_delivery_date: NotRequired[RFC3339DateTime]
    latest_estimated_delivery_date: NotRequired[RFC3339DateTime]
    rate: NotRequired[MoneyDict]
    shipping_service_options: NotRequired[ShippingServiceOptionsDict]
