from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class AcknowledgeOrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    status_code: Literal["Acknowledged"] = Field(default="Acknowledged", alias="statusCode")
    status_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="statusQuantity")


class AcknowledgeOrderLineDict(TypedDict):
    line_number: str
    status_code: Literal["Acknowledged"]
    status_quantity: NotRequired[QuantityWithUnitDict]
