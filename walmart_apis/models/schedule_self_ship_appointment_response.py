from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_self_ship_appointment_details import CommonSelfShipAppointmentDetails, CommonSelfShipAppointmentDetailsDict


class ScheduleSelfShipAppointmentResponse(SdkBaseModel):
    """The ``scheduleSelfShipAppointment`` response."""

    self_ship_appointment_details: CommonSelfShipAppointmentDetails = Field(alias="selfShipAppointmentDetails")
    """Appointment details for carrier pickup or Ship Node appointments."""


class ScheduleSelfShipAppointmentResponseDict(TypedDict):
    self_ship_appointment_details: CommonSelfShipAppointmentDetailsDict
