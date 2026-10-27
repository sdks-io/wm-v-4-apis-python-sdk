from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .settlement_period import SettlementPeriod, SettlementPeriodDict


class SettlementPeriodsResponse(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    periods: Optional[list[SettlementPeriod]] = UNSET


class SettlementPeriodsResponseDict(TypedDict):
    next_token: NotRequired[str]
    periods: NotRequired[list[SettlementPeriodDict]]
