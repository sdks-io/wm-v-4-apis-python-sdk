from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money_type_product_fees import MoneyTypeProductFees, MoneyTypeProductFeesDict


class FeeDetail(SdkBaseModel):
    """Estimated fee component. A fee component can include nested sub-fees in ``IncludedFeeDetailList``."""

    fee_type: str = Field(alias="FeeType")
    """Type of fee component, such as ``ReferralFee``, ``WFSFulfillmentFee``, or ``VariableClosingFee``."""

    fee_amount: MoneyTypeProductFees = Field(alias="FeeAmount")
    """Monetary amount and currency."""

    fee_promotion: Optional[MoneyTypeProductFees] = Field(default=UNSET, alias="FeePromotion")
    """Monetary amount and currency."""

    tax_amount: Optional[MoneyTypeProductFees] = Field(default=UNSET, alias="TaxAmount")
    """Monetary amount and currency."""

    final_fee: MoneyTypeProductFees = Field(alias="FinalFee")
    """Monetary amount and currency."""

    included_fee_detail_list: Optional[list[FeeDetail]] = Field(default=UNSET, alias="IncludedFeeDetailList")
    """Additional fee components included in this fee."""


class FeeDetailDict(TypedDict):
    fee_type: str
    fee_amount: MoneyTypeProductFeesDict
    fee_promotion: NotRequired[MoneyTypeProductFeesDict]
    tax_amount: NotRequired[MoneyTypeProductFeesDict]
    final_fee: MoneyTypeProductFeesDict
    included_fee_detail_list: NotRequired[list[FeeDetailDict]]
