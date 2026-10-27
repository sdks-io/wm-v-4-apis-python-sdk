from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload5 import Payload5, Payload5Dict


class CancelShipmentResponse1(SdkBaseModel):
    payload: Optional[Payload5] = UNSET


class CancelShipmentResponse1Dict(TypedDict):
    payload: NotRequired[Payload5Dict]
