from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipment import Shipment, ShipmentDict


class CancelShipmentResponse(SdkBaseModel):
    shipment: Optional[Shipment] = UNSET


class CancelShipmentResponseDict(TypedDict):
    shipment: NotRequired[ShipmentDict]
