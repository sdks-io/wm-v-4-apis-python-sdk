from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MoneyType1(SdkBaseModel):
    """Currency amount."""

    currency_code: str = Field(alias="CurrencyCode")
    """Three-digit currency code (ISO 4217)."""

    amount: float = Field(alias="Amount")


class MoneyType1Dict(TypedDict):
    currency_code: str
    amount: float
