from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class GenerateSelfShipAppointmentSlotsRequest(SdkBaseModel):
    """The ``generateSelfShipAppointmentSlots`` request."""

    desired_end_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="desiredEndDate")
    """The desired end date. In ISO 8601 datetime format."""

    desired_start_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="desiredStartDate")
    """The desired start date. In ISO 8601 datetime format."""


class GenerateSelfShipAppointmentSlotsRequestDict(TypedDict):
    desired_end_date: NotRequired[RFC3339DateTime]
    desired_start_date: NotRequired[RFC3339DateTime]
