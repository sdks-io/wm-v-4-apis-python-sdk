from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload21 import Payload21, Payload21Dict


class GetOrderAddressResponse(SdkBaseModel):
    payload: Optional[Payload21] = UNSET


class GetOrderAddressResponseDict(TypedDict):
    payload: NotRequired[Payload21Dict]
