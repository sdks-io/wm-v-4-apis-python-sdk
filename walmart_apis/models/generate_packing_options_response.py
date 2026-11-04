from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GeneratePackingOptionsResponse(SdkBaseModel):
    """The ``generatePackingOptions`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GeneratePackingOptionsResponseDict(TypedDict):
    operation_id: str
