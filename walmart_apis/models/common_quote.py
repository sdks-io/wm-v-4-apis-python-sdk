from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .common_currency import CommonCurrency, CommonCurrencyDict


class CommonQuote(SdkBaseModel):
    """The estimated shipping cost associated with the transportation option."""

    cost: CommonCurrency
    """The type and amount of currency."""

    expiration: Optional[RFC3339DateTime] = UNSET
    """The time at which this transportation option quote expires. In ISO 8601 datetime with pattern
    ``yyyy-MM-ddTHH:mm:ss.sssZ``."""

    voidable_until: Optional[RFC3339DateTime] = Field(default=UNSET, alias="voidableUntil")
    """Voidable until timestamp."""


class CommonQuoteDict(TypedDict):
    cost: CommonCurrencyDict
    expiration: NotRequired[RFC3339DateTime]
    voidable_until: NotRequired[RFC3339DateTime]
