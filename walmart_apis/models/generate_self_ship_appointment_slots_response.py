from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateSelfShipAppointmentSlotsResponse(SdkBaseModel):
    """The ``generateSelfShipAppointmentSlots`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GenerateSelfShipAppointmentSlotsResponseDict(TypedDict):
    operation_id: str
