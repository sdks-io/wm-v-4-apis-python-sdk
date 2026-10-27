from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_window import CommonWindow, CommonWindowDict


class CommonDates(SdkBaseModel):
    """Specifies the date that the seller expects their shipment will be shipped."""

    ready_to_ship_window: Optional[CommonWindow] = Field(default=UNSET, alias="readyToShipWindow")
    """Contains a start and end DateTime representing a time range."""


class CommonDatesDict(TypedDict):
    ready_to_ship_window: NotRequired[CommonWindowDict]
