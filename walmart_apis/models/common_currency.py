from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonCurrency(SdkBaseModel):
    """The type and amount of currency."""

    amount: float
    """Decimal value of the currency."""

    code: str
    """ISO 4217 standard currency code."""


class CommonCurrencyDict(TypedDict):
    amount: float
    code: str
