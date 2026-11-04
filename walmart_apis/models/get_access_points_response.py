from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload4 import Payload4, Payload4Dict


class GetAccessPointsResponse(SdkBaseModel):
    payload: Optional[Payload4] = UNSET


class GetAccessPointsResponseDict(TypedDict):
    payload: NotRequired[Payload4Dict]
