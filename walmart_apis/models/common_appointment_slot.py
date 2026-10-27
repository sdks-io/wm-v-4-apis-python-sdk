from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_appointment_slot_time import CommonAppointmentSlotTime, CommonAppointmentSlotTimeDict


class CommonAppointmentSlot(SdkBaseModel):
    """The Ship Node appointment slot for the transportation option."""

    slot_id: str = Field(alias="slotId")
    """An identifier to a self-ship appointment slot."""

    slot_time: CommonAppointmentSlotTime = Field(alias="slotTime")
    """An appointment slot time with start and end."""


class CommonAppointmentSlotDict(TypedDict):
    slot_id: str
    slot_time: CommonAppointmentSlotTimeDict
