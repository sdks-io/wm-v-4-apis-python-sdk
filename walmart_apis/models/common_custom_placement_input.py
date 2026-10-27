from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_item_input import CommonItemInput, CommonItemInputDict


class CommonCustomPlacementInput(SdkBaseModel):
    """Provide units going to the ship node."""

    items: list[CommonItemInput]
    """Items included while creating Inbound Plan."""

    warehouse_id: str = Field(alias="warehouseId")
    """Ship Node ID."""


class CommonCustomPlacementInputDict(TypedDict):
    items: list[CommonItemInputDict]
    warehouse_id: str
