from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class PickupWindow(SdkBaseModel):
    start: Optional[RFC3339DateTime] = UNSET
    end: Optional[RFC3339DateTime] = UNSET


class PickupWindowDict(TypedDict):
    start: NotRequired[RFC3339DateTime]
    end: NotRequired[RFC3339DateTime]
