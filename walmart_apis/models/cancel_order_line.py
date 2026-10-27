from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cancellation_reason import CancellationReasonOrStr
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class CancelOrderLine(SdkBaseModel):
    line_number: str = Field(alias="lineNumber")
    cancel_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="cancelQuantity")
    cancellation_reason: CancellationReasonOrStr = Field(alias="cancellationReason")


class CancelOrderLineDict(TypedDict):
    line_number: str
    cancel_quantity: NotRequired[QuantityWithUnitDict]
    cancellation_reason: CancellationReasonOrStr
