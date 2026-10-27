from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_currency import CommonCurrency, CommonCurrencyDict


class CommonPrepInstruction(SdkBaseModel):
    """Information pertaining to the preparation of inbound goods."""

    fee: Optional[CommonCurrency] = UNSET
    """The type and amount of currency."""

    prep_owner: Optional[str] = Field(default=UNSET, alias="prepOwner")
    """Owner of the preparations. Options include ``SELLER`` or ``NONE``."""

    prep_type: Optional[str] = Field(default=UNSET, alias="prepType")
    """Type of preparation that should be done."""


class CommonPrepInstructionDict(TypedDict):
    fee: NotRequired[CommonCurrencyDict]
    prep_owner: NotRequired[str]
    prep_type: NotRequired[str]
