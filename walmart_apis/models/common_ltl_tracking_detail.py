from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonLtlTrackingDetail(SdkBaseModel):
    """Contains information related to Less-Than-Truckload (LTL) shipment tracking."""

    bill_of_lading_number: Optional[str] = Field(default=UNSET, alias="billOfLadingNumber")
    """The number of the carrier shipment acknowledgement document."""

    freight_bill_number: Optional[list[str]] = Field(default=UNSET, alias="freightBillNumber")
    """The number associated with the freight bill."""


class CommonLtlTrackingDetailDict(TypedDict):
    bill_of_lading_number: NotRequired[str]
    freight_bill_number: NotRequired[list[str]]
