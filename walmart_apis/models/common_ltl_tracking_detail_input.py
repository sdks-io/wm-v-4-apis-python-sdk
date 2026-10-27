from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonLtlTrackingDetailInput(SdkBaseModel):
    """Contains input information to update LTL tracking information."""

    bill_of_lading_number: Optional[str] = Field(default=UNSET, alias="billOfLadingNumber")
    """The number of the carrier shipment acknowledgement document."""

    freight_bill_number: list[str] = Field(alias="freightBillNumber")
    """Number associated with the freight bill."""


class CommonLtlTrackingDetailInputDict(TypedDict):
    bill_of_lading_number: NotRequired[str]
    freight_bill_number: list[str]
