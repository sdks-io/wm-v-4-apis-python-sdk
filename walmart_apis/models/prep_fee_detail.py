from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.prep_instruction import PrepInstructionOrStr
from .prep_fee_amount import PrepFeeAmount, PrepFeeAmountDict


class PrepFeeDetail(SdkBaseModel):
    """The prep fee associated with a single prep instruction."""

    prep_instruction: Optional[PrepInstructionOrStr] = Field(default=UNSET, alias="prepInstruction")
    """A single preparation action applicable to an item."""

    fee_per_unit: Optional[PrepFeeAmount] = Field(default=UNSET, alias="feePerUnit")
    """A currency-denominated fee amount."""


class PrepFeeDetailDict(TypedDict):
    prep_instruction: NotRequired[PrepInstructionOrStr]
    fee_per_unit: NotRequired[PrepFeeAmountDict]
