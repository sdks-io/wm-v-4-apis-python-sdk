from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateDeliveryWindowOptionsResponse(SdkBaseModel):
    """The ``generateDeliveryWindowOptions`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GenerateDeliveryWindowOptionsResponseDict(TypedDict):
    operation_id: str
