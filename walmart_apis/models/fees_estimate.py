from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .fee_detail import FeeDetail, FeeDetailDict
from .money_type_product_fees import MoneyTypeProductFees, MoneyTypeProductFeesDict


class FeesEstimate(SdkBaseModel):
    """Estimated fees for the item, including the total estimate and individual fee components."""

    time_of_fees_estimation: RFC3339DateTime = Field(alias="TimeOfFeesEstimation")
    """Timestamp when the fees were estimated, in ISO 8601 format."""

    total_fees_estimate: MoneyTypeProductFees = Field(alias="TotalFeesEstimate")
    """Monetary amount and currency."""

    fee_detail_list: Optional[list[FeeDetail]] = Field(default=UNSET, alias="FeeDetailList")


class FeesEstimateDict(TypedDict):
    time_of_fees_estimation: RFC3339DateTime
    total_fees_estimate: MoneyTypeProductFeesDict
    fee_detail_list: NotRequired[list[FeeDetailDict]]
