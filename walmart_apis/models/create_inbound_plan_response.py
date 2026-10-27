from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateInboundPlanResponse(SdkBaseModel):
    """The ``createInboundPlan`` response."""

    inbound_plan_id: str = Field(alias="inboundPlanId")
    """Identifier of the newly created inbound plan."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class CreateInboundPlanResponseDict(TypedDict):
    inbound_plan_id: str
    operation_id: str
