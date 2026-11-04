from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CommonCarrierAppointment(SdkBaseModel):
    """Contains details for a transportation carrier appointment."""

    end_time: RFC3339DateTime = Field(alias="endTime")
    """The end timestamp of the appointment in UTC."""

    start_time: RFC3339DateTime = Field(alias="startTime")
    """The start timestamp of the appointment in UTC."""


class CommonCarrierAppointmentDict(TypedDict):
    end_time: RFC3339DateTime
    start_time: RFC3339DateTime
