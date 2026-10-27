from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CommonAppointmentSlotTime(SdkBaseModel):
    """An appointment slot time with start and end., Contains details for a transportation carrier appointment., An
    appointment slot time with start and end., Contains details for a transportation carrier appointment."""

    end_time: RFC3339DateTime = Field(alias="endTime")
    """The end timestamp of the appointment in UTC."""

    start_time: RFC3339DateTime = Field(alias="startTime")
    """The start timestamp of the appointment in UTC."""


class CommonAppointmentSlotTimeDict(TypedDict):
    end_time: RFC3339DateTime
    start_time: RFC3339DateTime
