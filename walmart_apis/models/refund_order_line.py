from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refund_type import RefundTypeOrStr
from .money import Money, MoneyDict


class RefundOrderLine(SdkBaseModel):
    """Refund details for a single order line."""

    line_number: str = Field(alias="lineNumber")
    refund_amount: Money = Field(alias="refundAmount")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    refund_type: RefundTypeOrStr = Field(alias="refundType")
    """Indicates whether the refund is issued for a return (``RETURN``), cancellation (``CANCELLATION``), or goodwill
    adjustment (``GOODWILL``)."""

    reason: Optional[str] = UNSET
    """Optional explanation for the refund, up to 500 characters. For example, "Customer returned item due to defect."
    """


class RefundOrderLineDict(TypedDict):
    line_number: str
    refund_amount: MoneyDict
    refund_type: RefundTypeOrStr
    reason: NotRequired[str]
