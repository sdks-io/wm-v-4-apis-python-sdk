from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.common_prep_category import CommonPrepCategoryOrStr
from .enums.common_prep_type import CommonPrepTypeOrStr


class CommonMskuPrepDetailInput(SdkBaseModel):
    """An MSKU and its related prep details (input)."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    prep_category: CommonPrepCategoryOrStr = Field(alias="prepCategory")
    """The preparation category for shipping an item to Walmart's fulfillment network."""

    prep_types: list[CommonPrepTypeOrStr] = Field(alias="prepTypes")
    """A list of preparation types associated with a preparation category."""


class CommonMskuPrepDetailInputDict(TypedDict):
    msku: str
    prep_category: CommonPrepCategoryOrStr
    prep_types: list[CommonPrepTypeOrStr]
