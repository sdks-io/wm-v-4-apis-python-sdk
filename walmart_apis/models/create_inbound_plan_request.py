from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_address_input import CommonAddressInput, CommonAddressInputDict
from .common_item_input import CommonItemInput, CommonItemInputDict


class CreateInboundPlanRequest(SdkBaseModel):
    """Request to create an inbound plan for shipping items to Walmart fulfillment centers."""

    destination_marketplaces: list[str] = Field(alias="destinationMarketplaces")
    """Walmart Marketplace identifiers for the destination of the planned shipment. Only one marketplace can be
    specified."""

    items: list[CommonItemInput]
    """Items to include in the inbound plan."""

    name: Optional[str] = UNSET
    """Human-readable name for the inbound plan. If omitted, a default name is assigned."""

    source_address: CommonAddressInput = Field(alias="sourceAddress")
    """Specific details to identify a place (input variant — phone required)."""


class CreateInboundPlanRequestDict(TypedDict):
    destination_marketplaces: list[str]
    items: list[CommonItemInputDict]
    name: NotRequired[str]
    source_address: CommonAddressInputDict
