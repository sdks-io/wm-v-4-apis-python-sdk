from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .settlement_transaction import SettlementTransaction, SettlementTransactionDict


class SettlementDetailsResponse(SdkBaseModel):
    next_token: Optional[str] = Field(default=UNSET, alias="nextToken")
    total_records: Optional[int] = Field(default=UNSET, alias="totalRecords")
    transactions: Optional[list[SettlementTransaction]] = UNSET


class SettlementDetailsResponseDict(TypedDict):
    next_token: NotRequired[str]
    total_records: NotRequired[int]
    transactions: NotRequired[list[SettlementTransactionDict]]
