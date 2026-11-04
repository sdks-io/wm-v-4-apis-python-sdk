from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateInboundPlanResponse(SdkBaseModel):
    """Response returned after creating an inbound plan."""

    inbound_plan_id: str = Field(alias="inboundPlanId")
    """Unique identifier of the newly created inbound plan."""

    operation_id: str = Field(alias="operationId")
    """Unique identifier for the given operation."""


class CreateInboundPlanResponseDict(TypedDict):
    inbound_plan_id: str
    operation_id: str
