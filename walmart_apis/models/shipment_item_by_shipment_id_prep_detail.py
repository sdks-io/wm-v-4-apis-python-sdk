from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShipmentItemByShipmentIdPrepDetail(SdkBaseModel):
    """One preparation instruction for a shipment item (upstream ``PrepDetailsList`` entry)."""

    prep_instruction: Optional[str] = Field(default=UNSET, alias="prepInstruction")
    """Preparation instruction type (Labeling or Polybagging)."""

    prep_owner: Optional[str] = Field(default=UNSET, alias="prepOwner")
    """Who performs the prep. Currently hardcoded to ``WALMART`` upstream."""


class ShipmentItemByShipmentIdPrepDetailDict(TypedDict):
    prep_instruction: NotRequired[str]
    prep_owner: NotRequired[str]
