from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_pagination import CommonPagination, CommonPaginationDict
from .common_self_ship_appointment_slots_availability import (
    CommonSelfShipAppointmentSlotsAvailability,
    CommonSelfShipAppointmentSlotsAvailabilityDict,
)


class GetSelfShipAppointmentSlotsResponse(SdkBaseModel):
    """The ``getSelfShipAppointmentSlots`` response."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""

    self_ship_appointment_slots_availability: CommonSelfShipAppointmentSlotsAvailability = Field(
        alias="selfShipAppointmentSlotsAvailability"
    )
    """The self ship appointment time slots availability and an expiration date for which the slots can be scheduled."""


class GetSelfShipAppointmentSlotsResponseDict(TypedDict):
    pagination: NotRequired[CommonPaginationDict]
    self_ship_appointment_slots_availability: CommonSelfShipAppointmentSlotsAvailabilityDict
