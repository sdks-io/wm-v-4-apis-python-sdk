from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .cancel_order_line import CancelOrderLine, CancelOrderLineDict


class CancelOrderLinesRequest(SdkBaseModel):
    """Order lines to cancel and associated reasons."""

    order_lines: list[CancelOrderLine] = Field(alias="orderLines")
    """Order lines to cancel."""


class CancelOrderLinesRequestDict(TypedDict):
    order_lines: list[CancelOrderLineDict]
