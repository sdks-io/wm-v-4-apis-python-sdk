from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.barcode_instruction import BarcodeInstructionOrStr
from .enums.prep_guidance import PrepGuidanceOrStr
from .enums.prep_instruction import PrepInstructionOrStr
from .prep_fee_detail import PrepFeeDetail, PrepFeeDetailDict


class SkuPrepInstructions(SdkBaseModel):
    """Prep instructions for a single seller SKU."""

    seller_sku: Optional[str] = Field(default=UNSET, alias="sellerSku")
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    asin: Optional[str] = UNSET
    """The Amazon Standard Identification Number associated with the seller SKU, if known."""

    barcode_instruction: Optional[BarcodeInstructionOrStr] = Field(default=UNSET, alias="barcodeInstruction")
    """Guidance on which barcode a seller should use when labeling an item."""

    prep_guidance: Optional[PrepGuidanceOrStr] = Field(default=UNSET, alias="prepGuidance")
    """High-level guidance on whether/how an item needs to be prepped."""

    prep_instruction_list: Optional[list[PrepInstructionOrStr]] = Field(default=UNSET, alias="prepInstructionList")
    """A list of preparation instructions applicable to this item."""

    prep_fees_details_list: Optional[list[PrepFeeDetail]] = Field(default=UNSET, alias="prepFeesDetailsList")
    """A list of prep fees applicable to this item, one entry per prep instruction."""


class SkuPrepInstructionsDict(TypedDict):
    seller_sku: NotRequired[str]
    asin: NotRequired[str]
    barcode_instruction: NotRequired[BarcodeInstructionOrStr]
    prep_guidance: NotRequired[PrepGuidanceOrStr]
    prep_instruction_list: NotRequired[list[PrepInstructionOrStr]]
    prep_fees_details_list: NotRequired[list[PrepFeeDetailDict]]
