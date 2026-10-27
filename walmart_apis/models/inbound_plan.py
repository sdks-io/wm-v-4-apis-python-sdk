from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .common_address import CommonAddress, CommonAddressDict
from .common_packing_option_summary import CommonPackingOptionSummary, CommonPackingOptionSummaryDict
from .common_placement_option_summary import CommonPlacementOptionSummary, CommonPlacementOptionSummaryDict
from .common_shipment_summary import CommonShipmentSummary, CommonShipmentSummaryDict


class InboundPlan(SdkBaseModel):
    """Inbound plan containing details of the WFS inbound workflow."""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The time at which the inbound plan was created. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ssZ``."""

    inbound_plan_id: str = Field(alias="inboundPlanId")
    """Identifier of an inbound plan."""

    last_updated_at: RFC3339DateTime = Field(alias="lastUpdatedAt")
    """The time at which the inbound plan was last updated. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ssZ``."""

    marketplace_ids: list[str] = Field(alias="marketplaceIds")
    """A list of Walmart marketplace IDs."""

    name: str
    """Human-readable name of the inbound plan."""

    packing_options: Optional[list[CommonPackingOptionSummary]] = Field(default=UNSET, alias="packingOptions")
    """Packing options for the inbound plan. Populated after generation via the corresponding operation."""

    placement_options: Optional[list[CommonPlacementOptionSummary]] = Field(default=UNSET, alias="placementOptions")
    """Placement options for the inbound plan. Populated after generation via the corresponding operation."""

    shipments: Optional[list[CommonShipmentSummary]] = UNSET
    """A list of shipment IDs for the inbound plan. Populated after ``confirmPlacementOptions``."""

    source_address: CommonAddress = Field(alias="sourceAddress")
    """Specific details to identify a place."""

    status: str
    """Current status of the inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``."""


class InboundPlanDict(TypedDict):
    created_at: RFC3339DateTime
    inbound_plan_id: str
    last_updated_at: RFC3339DateTime
    marketplace_ids: list[str]
    name: str
    packing_options: NotRequired[list[CommonPackingOptionSummaryDict]]
    placement_options: NotRequired[list[CommonPlacementOptionSummaryDict]]
    shipments: NotRequired[list[CommonShipmentSummaryDict]]
    source_address: CommonAddressDict
    status: str
