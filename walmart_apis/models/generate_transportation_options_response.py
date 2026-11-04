from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateTransportationOptionsResponse(SdkBaseModel):
    """The ``generateTransportationOptions`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GenerateTransportationOptionsResponseDict(TypedDict):
    operation_id: str
