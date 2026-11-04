from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelSelfShipAppointmentResponse(SdkBaseModel):
    """The ``cancelSelfShipAppointment`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class CancelSelfShipAppointmentResponseDict(TypedDict):
    operation_id: str
