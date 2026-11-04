from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PrepFeeAmount(SdkBaseModel):
    """A currency-denominated fee amount."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The ISO 4217 three-letter currency code."""

    value: Optional[float] = UNSET
    """The fee amount, in the given currency."""


class PrepFeeAmountDict(TypedDict):
    currency_code: NotRequired[str]
    value: NotRequired[float]
