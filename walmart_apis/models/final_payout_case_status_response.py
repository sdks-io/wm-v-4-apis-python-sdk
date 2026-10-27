from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status21 import Status21OrStr
from .money import Money, MoneyDict


class FinalPayoutCaseStatusResponse(SdkBaseModel):
    case_id: Optional[str] = Field(default=UNSET, alias="caseId")
    status: Optional[Status21OrStr] = UNSET
    amount: Optional[Money] = UNSET


class FinalPayoutCaseStatusResponseDict(TypedDict):
    case_id: NotRequired[str]
    status: NotRequired[Status21OrStr]
    amount: NotRequired[MoneyDict]
