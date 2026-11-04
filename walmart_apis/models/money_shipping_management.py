from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class MoneyShippingManagement(SdkBaseModel):
    """Canonical monetary amount (string value + ISO currency code)."""

    amount: Optional[str] = UNSET
    """Monetary amount as a string to preserve precision."""

    currency_code: str = Field(default="USD", alias="currencyCode")
    """ISO 4217 currency code."""


class MoneyShippingManagementDict(TypedDict):
    amount: NotRequired[str]
    currency_code: NotRequired[str]
