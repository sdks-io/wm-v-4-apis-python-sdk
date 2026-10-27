from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload31 import Payload31, Payload31Dict


class GetTrackingResponse(SdkBaseModel):
    payload: Optional[Payload31] = UNSET


class GetTrackingResponseDict(TypedDict):
    payload: NotRequired[Payload31Dict]
