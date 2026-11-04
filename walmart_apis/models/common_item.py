from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_prep_instruction import CommonPrepInstruction, CommonPrepInstructionDict


class CommonItem(SdkBaseModel):
    """Information associated with a single SKU in the seller's catalog."""

    msku: str
    """The merchant-defined SKU ID (upstream Inbound Order Workflow ``sku``; also referred to as ``sellerSku`` in Amazon
    SP-API-parity contexts)."""

    asin: Optional[str] = UNSET
    """Walmart item number (upstream ``itemId``, sourced from ``poLines.itemNbr``), exposed under the Amazon
    SP-API-parity ``asin`` name for this shared item shape. Optional; not populated on every list surface."""

    fnsku: Optional[str] = UNSET
    """Global Trade Item Number for this item (upstream ``gtin``). Optional; not populated on every list surface."""

    expiration: Optional[str] = UNSET
    """The expiration date of the MSKU. In ISO 8601 date format with pattern ``YYYY-MM-DD``. The same MSKU with
    different expiration dates cannot go into the same box."""

    label_owner: str = Field(alias="labelOwner")
    """Specifies who will label the items (upstream Inbound Order Workflow ``labelOwner``, e.g. ``SELLER``, ``WALMART``,
    or ``NONE``)."""

    manufacturing_lot_code: Optional[str] = Field(default=UNSET, alias="manufacturingLotCode")
    """The manufacturing lot code."""

    prep_instructions: list[CommonPrepInstruction] = Field(alias="prepInstructions")
    """Special preparations that are required for an item."""

    quantity: int
    """The number of the specified MSKU."""


class CommonItemDict(TypedDict):
    msku: str
    asin: NotRequired[str]
    fnsku: NotRequired[str]
    expiration: NotRequired[str]
    label_owner: str
    manufacturing_lot_code: NotRequired[str]
    prep_instructions: list[CommonPrepInstructionDict]
    quantity: int
