from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .acknowledge_order_line import AcknowledgeOrderLine, AcknowledgeOrderLineDict


class AcknowledgeOrderRequest(SdkBaseModel):
    order_lines: list[AcknowledgeOrderLine] = Field(alias="orderLines")


class AcknowledgeOrderRequestDict(TypedDict):
    order_lines: list[AcknowledgeOrderLineDict]
