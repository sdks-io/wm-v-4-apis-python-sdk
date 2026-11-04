from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateShipmentSourceAddressResponse(SdkBaseModel):
    """The ``updateShipmentSourceAddress`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class UpdateShipmentSourceAddressResponseDict(TypedDict):
    operation_id: str
