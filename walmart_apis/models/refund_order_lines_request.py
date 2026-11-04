from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .refund_order_line import RefundOrderLine, RefundOrderLineDict


class RefundOrderLinesRequest(SdkBaseModel):
    """Order lines and amounts to refund."""

    order_lines: list[RefundOrderLine] = Field(alias="orderLines")
    """Order lines for which refunds are requested."""


class RefundOrderLinesRequestDict(TypedDict):
    order_lines: list[RefundOrderLineDict]
