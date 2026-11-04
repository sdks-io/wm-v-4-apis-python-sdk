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
    """Owner of the preparation (upstream Inbound Order Workflow ``prepOwner``). Options include ``SELLER``,
    ``WALMART``, or ``NONE``."""

    prep_type: Optional[str] = Field(default=UNSET, alias="prepType")
    """Type of preparation that should be done (upstream Inbound Order Workflow ``prepType``). WFS currently supports
    Labeling and Polybagging in practice; ``listInboundPlanItems`` formally enumerates this same concept as ``BAG``,
    ``TAPE``, ``WRAP``, ``LABEL``."""


class CommonPrepInstructionDict(TypedDict):
    fee: NotRequired[CommonCurrencyDict]
    prep_owner: NotRequired[str]
    prep_type: NotRequired[str]
