from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_shipping_management import AddressShippingManagement, AddressShippingManagementDict
from .supply_source_configuration import SupplySourceConfiguration, SupplySourceConfigurationDict


class CreateSupplySourceRequest(SdkBaseModel):
    supply_source_code: str = Field(alias="supplySourceCode")
    """Human-readable name for the new supply source."""

    alias: Optional[str] = UNSET
    """Custom node identifier."""

    node_type: Optional[str] = Field(default=UNSET, alias="nodeType")
    """Type of node (e.g. ThreePL, DropShip)."""

    status: Optional[str] = UNSET
    """Initial status of the supply source. Known values: ACTIVE, INACTIVE. No enum declared -- see the note on
    SupplySource.status."""

    address: AddressShippingManagement
    """A postal address. Canonical shared shape -- see com.walmart.seller.core.model.Address's Javadoc (seller-api-core)
    for the full rationale and per-field examples."""

    configuration: Optional[SupplySourceConfiguration] = UNSET
    """Operating settings for the supply source — time zone and the processing calendar."""


class CreateSupplySourceRequestDict(TypedDict):
    supply_source_code: str
    alias: NotRequired[str]
    node_type: NotRequired[str]
    status: NotRequired[str]
    address: AddressShippingManagementDict
    configuration: NotRequired[SupplySourceConfigurationDict]
