from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cancel_order_line import CancelOrderLine, CancelOrderLineDict


class CancelOrderLinesRequest(SdkBaseModel):
    order_lines: list[CancelOrderLine] = Field(alias="orderLines")


class CancelOrderLinesRequestDict(TypedDict):
    order_lines: list[CancelOrderLineDict]
