from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateSupplySourceResponse(SdkBaseModel):
    supply_source_id: Optional[str] = Field(default=UNSET, alias="supplySourceId")
    """ID of the newly created supply source."""

    supply_source_code: Optional[str] = Field(default=UNSET, alias="supplySourceCode")
    """Name of the newly created supply source."""


class CreateSupplySourceResponseDict(TypedDict):
    supply_source_id: NotRequired[str]
    supply_source_code: NotRequired[str]
