from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MoneyTypeProductFees(SdkBaseModel):
    """Monetary amount and currency."""

    currency_code: str = Field(alias="CurrencyCode")
    """Three-letter ISO 4217 currency code."""

    amount: float = Field(alias="Amount")
    """Monetary amount."""


class MoneyTypeProductFeesDict(TypedDict):
    currency_code: str
    amount: float
