from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .fee_detail import FeeDetail, FeeDetailDict
from .money_type1 import MoneyType1, MoneyType1Dict


class FeesEstimate(SdkBaseModel):
    """The estimated fees broken down by component. Mirrors SP-API FeesEstimate."""

    time_of_fees_estimation: RFC3339DateTime = Field(alias="TimeOfFeesEstimation")
    total_fees_estimate: MoneyType1 = Field(alias="TotalFeesEstimate")
    """Currency amount."""

    fee_detail_list: Optional[list[FeeDetail]] = Field(default=UNSET, alias="FeeDetailList")


class FeesEstimateDict(TypedDict):
    time_of_fees_estimation: RFC3339DateTime
    total_fees_estimate: MoneyType1Dict
    fee_detail_list: NotRequired[list[FeeDetailDict]]
