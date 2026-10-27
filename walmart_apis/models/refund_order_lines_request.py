from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .refund_order_line import RefundOrderLine, RefundOrderLineDict


class RefundOrderLinesRequest(SdkBaseModel):
    order_lines: list[RefundOrderLine] = Field(alias="orderLines")


class RefundOrderLinesRequestDict(TypedDict):
    order_lines: list[RefundOrderLineDict]
