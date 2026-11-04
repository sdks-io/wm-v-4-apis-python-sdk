from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Money(SdkBaseModel):
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    amount: Optional[str] = UNSET
    """Monetary amount as string to preserve precision"""

    currency_code: str = Field(default="USD", alias="currencyCode")
    """ISO 4217 three-letter currency code."""


class MoneyDict(TypedDict):
    amount: NotRequired[str]
    currency_code: NotRequired[str]
