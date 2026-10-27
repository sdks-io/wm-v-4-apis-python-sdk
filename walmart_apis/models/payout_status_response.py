from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status11 import Status11OrStr
from .money import Money, MoneyDict


class PayoutStatusResponse(SdkBaseModel):
    status: Optional[Status11OrStr] = UNSET
    amount: Optional[Money] = UNSET
    scheduled_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="scheduledDate")
    completed_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="completedDate")


class PayoutStatusResponseDict(TypedDict):
    status: NotRequired[Status11OrStr]
    amount: NotRequired[MoneyDict]
    scheduled_date: NotRequired[RFC3339DateTime]
    completed_date: NotRequired[RFC3339DateTime]
