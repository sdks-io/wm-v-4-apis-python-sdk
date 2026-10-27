from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .common_address import CommonAddress, CommonAddressDict


class CommonInboundPlanSummary(SdkBaseModel):
    """A light-weight inbound plan."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The time at which the inbound plan was created. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ssZ``."""

    inbound_plan_id: str = Field(alias="inboundPlanId")
    """Identifier of an inbound plan."""

    last_updated_at: RFC3339DateTime = Field(alias="lastUpdatedAt")
    """The time at which the inbound plan was last updated. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ssZ``."""

    marketplace_ids: list[str] = Field(alias="marketplaceIds")
    """A list of Walmart marketplace IDs associated with this inbound plan."""

    name: str
    """Human-readable name of the inbound plan."""

    source_address: CommonAddress = Field(alias="sourceAddress")
    """Specific details to identify a place."""

    status: str
    """The current status of the inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``."""


class CommonInboundPlanSummaryDict(TypedDict):
    created_at: RFC3339DateTime
    inbound_plan_id: str
    last_updated_at: RFC3339DateTime
    marketplace_ids: list[str]
    name: str
    source_address: CommonAddressDict
    status: str
