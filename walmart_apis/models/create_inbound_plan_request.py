from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_address_input import CommonAddressInput, CommonAddressInputDict
from .common_item_input import CommonItemInput, CommonItemInputDict


class CreateInboundPlanRequest(SdkBaseModel):
    """The ``createInboundPlan`` request."""

    destination_marketplaces: list[str] = Field(alias="destinationMarketplaces")
    """Walmart Marketplace IDs where the items need to be shipped to. Currently only one marketplace can be selected."""

    items: list[CommonItemInput]
    """Items included in this plan."""

    name: Optional[str] = UNSET
    """Name for the Inbound Plan. If one isn't provided, a default name will be provided."""

    source_address: CommonAddressInput = Field(alias="sourceAddress")
    """Specific details to identify a place (input variant — phone required)."""


class CreateInboundPlanRequestDict(TypedDict):
    destination_marketplaces: list[str]
    items: list[CommonItemInputDict]
    name: NotRequired[str]
    source_address: CommonAddressInputDict
