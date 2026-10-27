from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class InitiatePayoutResponse(SdkBaseModel):
    payout_id: Optional[str] = Field(default=UNSET, alias="payoutId")
    status: Optional[str] = UNSET
    amount: Optional[Money] = UNSET


class InitiatePayoutResponseDict(TypedDict):
    payout_id: NotRequired[str]
    status: NotRequired[str]
    amount: NotRequired[MoneyDict]
