from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.barcode_instruction import BarcodeInstructionOrStr
from .enums.prep_guidance import PrepGuidanceOrStr
from .enums.prep_instruction import PrepInstructionOrStr


class AsinPrepInstructions(SdkBaseModel):
    """Prep instructions for a single ASIN."""

    asin: Optional[str] = UNSET
    """The Amazon Standard Identification Number."""

    barcode_instruction: Optional[BarcodeInstructionOrStr] = Field(default=UNSET, alias="barcodeInstruction")
    """Guidance on which barcode a seller should use when labeling an item."""

    prep_guidance: Optional[PrepGuidanceOrStr] = Field(default=UNSET, alias="prepGuidance")
    """High-level guidance on whether/how an item needs to be prepped."""

    prep_instruction_list: Optional[list[PrepInstructionOrStr]] = Field(default=UNSET, alias="prepInstructionList")
    """A list of preparation instructions applicable to this item."""


class AsinPrepInstructionsDict(TypedDict):
    asin: NotRequired[str]
    barcode_instruction: NotRequired[BarcodeInstructionOrStr]
    prep_guidance: NotRequired[PrepGuidanceOrStr]
    prep_instruction_list: NotRequired[list[PrepInstructionOrStr]]
