from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status2 import Status2OrStr
from .money import Money, MoneyDict


class FinalPayoutCaseStatusResponse(SdkBaseModel):
    case_id: Optional[str] = Field(default=UNSET, alias="caseId")
    status: Optional[Status2OrStr] = UNSET
    amount: Optional[Money] = UNSET
    """Canonical monetary amount (string value + ISO 4217 currency code)."""


class FinalPayoutCaseStatusResponseDict(TypedDict):
    case_id: NotRequired[str]
    status: NotRequired[Status2OrStr]
    amount: NotRequired[MoneyDict]
