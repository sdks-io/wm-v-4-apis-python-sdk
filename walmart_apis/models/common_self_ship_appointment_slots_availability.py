from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .common_appointment_slot import CommonAppointmentSlot, CommonAppointmentSlotDict


class CommonSelfShipAppointmentSlotsAvailability(SdkBaseModel):
    """The self ship appointment time slots availability and an expiration date for which the slots can be scheduled."""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The time at which the self ship appointment slot expires. In ISO 8601 datetime format."""

    slots: Optional[list[CommonAppointmentSlot]] = UNSET
    """A list of appointment slots."""


class CommonSelfShipAppointmentSlotsAvailabilityDict(TypedDict):
    expires_at: NotRequired[RFC3339DateTime]
    slots: NotRequired[list[CommonAppointmentSlotDict]]
