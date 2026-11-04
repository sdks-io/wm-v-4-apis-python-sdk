from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .acknowledge_order_line import AcknowledgeOrderLine, AcknowledgeOrderLineDict


class AcknowledgeOrderRequest(SdkBaseModel):
    """Order lines to acknowledge."""

    order_lines: list[AcknowledgeOrderLine] = Field(alias="orderLines")
    """Order lines to acknowledge."""


class AcknowledgeOrderRequestDict(TypedDict):
    order_lines: list[AcknowledgeOrderLineDict]
