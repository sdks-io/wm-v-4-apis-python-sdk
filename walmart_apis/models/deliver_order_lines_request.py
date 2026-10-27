from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .deliver_order_line import DeliverOrderLine, DeliverOrderLineDict


class DeliverOrderLinesRequest(SdkBaseModel):
    order_lines: list[DeliverOrderLine] = Field(alias="orderLines")


class DeliverOrderLinesRequestDict(TypedDict):
    order_lines: list[DeliverOrderLineDict]
