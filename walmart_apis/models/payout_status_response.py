from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.status1_payments import Status1PaymentsOrStr
from .money import Money, MoneyDict


class PayoutStatusResponse(SdkBaseModel):
    status: Optional[Status1PaymentsOrStr] = UNSET
    amount: Optional[Money] = UNSET
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    scheduled_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="scheduledDate")
    completed_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="completedDate")


class PayoutStatusResponseDict(TypedDict):
    status: NotRequired[Status1PaymentsOrStr]
    amount: NotRequired[MoneyDict]
    scheduled_date: NotRequired[RFC3339DateTime]
    completed_date: NotRequired[RFC3339DateTime]
