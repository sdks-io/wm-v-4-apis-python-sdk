from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.cancellation_reason import CancellationReasonOrStr
from .quantity_with_unit import QuantityWithUnit, QuantityWithUnitDict


class CancelOrderLine(SdkBaseModel):
    """Order line and reason for cancellation."""

    line_number: str = Field(alias="lineNumber")
    """Line identifier within the purchase order."""

    cancel_quantity: Optional[QuantityWithUnit] = Field(default=UNSET, alias="cancelQuantity")
    """Numeric quantity and its unit of measure."""

    cancellation_reason: CancellationReasonOrStr = Field(alias="cancellationReason")
    """Reason for canceling the order line."""


class CancelOrderLineDict(TypedDict):
    line_number: str
    cancel_quantity: NotRequired[QuantityWithUnitDict]
    cancellation_reason: CancellationReasonOrStr
