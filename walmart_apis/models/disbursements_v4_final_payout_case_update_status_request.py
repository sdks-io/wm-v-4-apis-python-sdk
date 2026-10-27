from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status3 import Status3OrStr


class DisbursementsV4FinalPayoutCaseUpdateStatusRequest(SdkBaseModel):
    status: Status3OrStr
    notes: Optional[str] = UNSET


class DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict(TypedDict):
    status: Status3OrStr
    notes: NotRequired[str]
