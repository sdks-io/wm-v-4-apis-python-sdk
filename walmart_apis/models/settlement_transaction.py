from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .money import Money, MoneyDict


class SettlementTransaction(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    transaction_type: Optional[str] = Field(default=UNSET, alias="transactionType")
    amount: Optional[Money] = UNSET
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    posted_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="postedDate")


class SettlementTransactionDict(TypedDict):
    purchase_order_id: NotRequired[str]
    transaction_type: NotRequired[str]
    amount: NotRequired[MoneyDict]
    posted_date: NotRequired[RFC3339DateTime]
