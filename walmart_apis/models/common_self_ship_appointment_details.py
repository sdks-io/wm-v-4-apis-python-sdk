from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_appointment_slot_time import CommonAppointmentSlotTime, CommonAppointmentSlotTimeDict


class CommonSelfShipAppointmentDetails(SdkBaseModel):
    """Appointment details for carrier pickup or Ship Node appointments."""

    appointment_id: Optional[float] = Field(default=UNSET, alias="appointmentId")
    """Identifier for appointment."""

    appointment_slot_time: Optional[CommonAppointmentSlotTime] = Field(default=UNSET, alias="appointmentSlotTime")
    """An appointment slot time with start and end."""

    appointment_status: Optional[str] = Field(default=UNSET, alias="appointmentStatus")
    """Status of the appointment."""


class CommonSelfShipAppointmentDetailsDict(TypedDict):
    appointment_id: NotRequired[float]
    appointment_slot_time: NotRequired[CommonAppointmentSlotTimeDict]
    appointment_status: NotRequired[str]
