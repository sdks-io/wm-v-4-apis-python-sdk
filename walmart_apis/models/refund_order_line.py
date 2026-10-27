from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.refund_type import RefundTypeOrStr
from .money import Money, MoneyDict


class RefundOrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    refund_amount: Money = Field(alias="refundAmount")
    refund_type: RefundTypeOrStr = Field(alias="refundType")
    """Why the refund is being issued. Compressed from gmp-orders-mono's 22-entry ``RefundReason`` enum to the three
    classes that actually drive downstream behaviour today (return-flow vs cancel-flow vs goodwill-credit). Free-form
    sub-reason goes in ``reason``."""

    reason: Optional[str] = UNSET
    """Optional free-form note (e.g. "item arrived damaged")."""


class RefundOrderLineDict(TypedDict):
    line_number: str
    refund_amount: MoneyDict
    refund_type: RefundTypeOrStr
    reason: NotRequired[str]
