from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ship_order_line import ShipOrderLine, ShipOrderLineDict


class ShipOrderLinesRequest(SdkBaseModel):
    """Order lines and tracking information for a shipment."""

    order_lines: list[ShipOrderLine] = Field(alias="orderLines")
    """Order lines included in the shipment."""


class ShipOrderLinesRequestDict(TypedDict):
    order_lines: list[ShipOrderLineDict]
