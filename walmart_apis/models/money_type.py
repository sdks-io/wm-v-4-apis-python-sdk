from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MoneyType(SdkBaseModel):
    """Currency type and monetary value."""

    currency_code: str = Field(default="USD", alias="CurrencyCode")
    """The currency code in ISO 4217 format."""

    amount: Optional[float] = Field(default=UNSET, alias="Amount")
    """The monetary value."""


class MoneyTypeDict(TypedDict):
    currency_code: NotRequired[str]
    amount: NotRequired[float]
