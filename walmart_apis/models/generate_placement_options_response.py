from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GeneratePlacementOptionsResponse(SdkBaseModel):
    """The ``generatePlacementOptions`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GeneratePlacementOptionsResponseDict(TypedDict):
    operation_id: str
