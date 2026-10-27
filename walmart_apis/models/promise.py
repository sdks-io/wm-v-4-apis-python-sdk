from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .delivery_window import DeliveryWindow, DeliveryWindowDict
from .pickup_window import PickupWindow, PickupWindowDict


class Promise(SdkBaseModel):
    delivery_window: Optional[DeliveryWindow] = Field(default=UNSET, alias="deliveryWindow")
    pickup_window: Optional[PickupWindow] = Field(default=UNSET, alias="pickupWindow")


class PromiseDict(TypedDict):
    delivery_window: NotRequired[DeliveryWindowDict]
    pickup_window: NotRequired[PickupWindowDict]
