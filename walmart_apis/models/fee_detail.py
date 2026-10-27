from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type1 import MoneyType1, MoneyType1Dict


class FeeDetail(SdkBaseModel):
    """Detail for a single fee component. May nest sub-fees in IncludedFeeDetailList. Mirrors SP-API FeeDetail."""

    fee_type: str = Field(alias="FeeType")
    """Fee type, e.g. ReferralFee, WFSFulfillmentFee, VariableClosingFee."""

    fee_amount: MoneyType1 = Field(alias="FeeAmount")
    """Currency amount."""

    fee_promotion: Optional[MoneyType1] = Field(default=UNSET, alias="FeePromotion")
    """Currency amount."""

    tax_amount: Optional[MoneyType1] = Field(default=UNSET, alias="TaxAmount")
    """Currency amount."""

    final_fee: MoneyType1 = Field(alias="FinalFee")
    """Currency amount."""


class FeeDetailDict(TypedDict):
    fee_type: str
    fee_amount: MoneyType1Dict
    fee_promotion: NotRequired[MoneyType1Dict]
    tax_amount: NotRequired[MoneyType1Dict]
    final_fee: MoneyType1Dict
