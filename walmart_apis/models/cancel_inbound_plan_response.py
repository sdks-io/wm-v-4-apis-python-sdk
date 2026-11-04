from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelInboundPlanResponse(SdkBaseModel):
    """Response returned after canceling an inbound plan."""

    operation_id: str = Field(alias="operationId")
    """Unique identifier for the given operation."""


class CancelInboundPlanResponseDict(TypedDict):
    operation_id: str
