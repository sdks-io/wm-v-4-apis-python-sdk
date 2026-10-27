from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_prep_instruction import CommonPrepInstruction, CommonPrepInstructionDict


class CommonItem(SdkBaseModel):
    """Information associated with a single SKU in the seller's catalog."""

    msku: str
    """The merchant-defined SKU ID."""

    expiration: Optional[str] = UNSET
    """The expiration date of the MSKU. In ISO 8601 date format with pattern ``YYYY-MM-DD``. The same MSKU with
    different expiration dates cannot go into the same box."""

    label_owner: str = Field(alias="labelOwner")
    """Specifies who will label the items. Options include ``SELLER`` and ``NONE``."""

    manufacturing_lot_code: Optional[str] = Field(default=UNSET, alias="manufacturingLotCode")
    """The manufacturing lot code."""

    prep_instructions: list[CommonPrepInstruction] = Field(alias="prepInstructions")
    """Special preparations that are required for an item."""

    quantity: int
    """The number of the specified MSKU."""


class CommonItemDict(TypedDict):
    msku: str
    expiration: NotRequired[str]
    label_owner: str
    manufacturing_lot_code: NotRequired[str]
    prep_instructions: list[CommonPrepInstructionDict]
    quantity: int
