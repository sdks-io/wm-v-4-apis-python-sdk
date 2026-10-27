from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload6 import Payload6, Payload6Dict


class GetAccessPointsResponse(SdkBaseModel):
    payload: Optional[Payload6] = UNSET


class GetAccessPointsResponseDict(TypedDict):
    payload: NotRequired[Payload6Dict]
