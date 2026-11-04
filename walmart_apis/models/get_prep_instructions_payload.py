from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .asin_prep_instructions import AsinPrepInstructions, AsinPrepInstructionsDict
from .invalid_asin_detail import InvalidAsinDetail, InvalidAsinDetailDict
from .invalid_sku_detail import InvalidSkuDetail, InvalidSkuDetailDict
from .sku_prep_instructions import SkuPrepInstructions, SkuPrepInstructionsDict


class GetPrepInstructionsPayload(SdkBaseModel):
    """The payload of the ``getPrepInstructions`` response."""

    sku_prep_instructions_list: Optional[list[SkuPrepInstructions]] = Field(
        default=UNSET, alias="skuPrepInstructionsList"
    )
    """A list of prep instructions for the requested seller SKUs."""

    invalid_sku_list: Optional[list[InvalidSkuDetail]] = Field(default=UNSET, alias="invalidSkuList")
    """A list of requested seller SKUs that could not be resolved."""

    asin_prep_instructions_list: Optional[list[AsinPrepInstructions]] = Field(
        default=UNSET, alias="asinPrepInstructionsList"
    )
    """A list of prep instructions for the requested ASINs."""

    invalid_asin_list: Optional[list[InvalidAsinDetail]] = Field(default=UNSET, alias="invalidAsinList")
    """A list of requested ASINs that could not be resolved."""


class GetPrepInstructionsPayloadDict(TypedDict):
    sku_prep_instructions_list: NotRequired[list[SkuPrepInstructionsDict]]
    invalid_sku_list: NotRequired[list[InvalidSkuDetailDict]]
    asin_prep_instructions_list: NotRequired[list[AsinPrepInstructionsDict]]
    invalid_asin_list: NotRequired[list[InvalidAsinDetailDict]]
