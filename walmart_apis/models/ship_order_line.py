from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict
from .tracking_info import TrackingInfo, TrackingInfoDict


class ShipOrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    ship_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="shipQuantity")
    tracking_info: TrackingInfo = Field(alias="trackingInfo")


class ShipOrderLineDict(TypedDict):
    line_number: str
    ship_quantity: NotRequired[QuantityWithUnitDict]
    tracking_info: TrackingInfoDict
