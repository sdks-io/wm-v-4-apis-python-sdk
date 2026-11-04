from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateShipmentTrackingDetailsResponse(SdkBaseModel):
    """The ``updateShipmentTrackingDetails`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class UpdateShipmentTrackingDetailsResponseDict(TypedDict):
    operation_id: str
