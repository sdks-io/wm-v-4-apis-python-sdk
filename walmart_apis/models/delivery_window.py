from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class DeliveryWindow(SdkBaseModel):
    start: Optional[RFC3339DateTime] = UNSET
    end: Optional[RFC3339DateTime] = UNSET


class DeliveryWindowDict(TypedDict):
    start: NotRequired[RFC3339DateTime]
    end: NotRequired[RFC3339DateTime]
