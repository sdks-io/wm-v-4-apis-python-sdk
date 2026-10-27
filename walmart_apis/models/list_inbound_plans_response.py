from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_inbound_plan_summary import CommonInboundPlanSummary, CommonInboundPlanSummaryDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListInboundPlansResponse(SdkBaseModel):
    """The ``listInboundPlans`` response."""

    inbound_plans: Optional[list[CommonInboundPlanSummary]] = Field(default=UNSET, alias="inboundPlans")
    """A list of inbound plans with minimal information."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListInboundPlansResponseDict(TypedDict):
    inbound_plans: NotRequired[list[CommonInboundPlanSummaryDict]]
    pagination: NotRequired[CommonPaginationDict]
