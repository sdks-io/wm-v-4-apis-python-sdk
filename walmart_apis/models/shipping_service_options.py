from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.carrier_will_pick_up_option import CarrierWillPickUpOptionOrStr
from .enums.delivery_experience import DeliveryExperienceOrStr
from .money import Money, MoneyDict


class ShippingServiceOptions(SdkBaseModel):
    delivery_experience: Optional[DeliveryExperienceOrStr] = Field(default=UNSET, alias="deliveryExperience")
    carrier_will_pick_up: Optional[bool] = Field(default=UNSET, alias="carrierWillPickUp")
    carrier_will_pick_up_option: Optional[CarrierWillPickUpOptionOrStr] = Field(
        default=UNSET, alias="carrierWillPickUpOption"
    )
    declared_value: Optional[Money] = Field(default=UNSET, alias="declaredValue")


class ShippingServiceOptionsDict(TypedDict):
    delivery_experience: NotRequired[DeliveryExperienceOrStr]
    carrier_will_pick_up: NotRequired[bool]
    carrier_will_pick_up_option: NotRequired[CarrierWillPickUpOptionOrStr]
    declared_value: NotRequired[MoneyDict]
