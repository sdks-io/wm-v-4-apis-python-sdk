from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ship_order_line import ShipOrderLine, ShipOrderLineDict


class ShipOrderLinesRequest(SdkBaseModel):
    order_lines: list[ShipOrderLine] = Field(alias="orderLines")


class ShipOrderLinesRequestDict(TypedDict):
    order_lines: list[ShipOrderLineDict]
