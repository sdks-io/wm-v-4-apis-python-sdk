from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_shipping_management import AddressShippingManagement, AddressShippingManagementDict
from .supply_source_configuration import SupplySourceConfiguration, SupplySourceConfigurationDict


class UpdateSupplySourceRequest(SdkBaseModel):
    supply_source_code: Optional[str] = Field(default=UNSET, alias="supplySourceCode")
    """Updated name."""

    alias: Optional[str] = UNSET
    """Updated custom node identifier."""

    node_type: Optional[str] = Field(default=UNSET, alias="nodeType")
    status: Optional[str] = UNSET
    """Updated status of the supply source. Known values: ACTIVE, INACTIVE. Toggling this is how an FC is deactivated;
    there is no archived state today. No enum declared -- see the note on SupplySource.status."""

    address: Optional[AddressShippingManagement] = UNSET
    """A postal address. Canonical shared shape -- see com.walmart.seller.core.model.Address's Javadoc (seller-api-core)
    for the full rationale and per-field examples."""

    configuration: Optional[SupplySourceConfiguration] = UNSET
    """Operating settings for the supply source — time zone and the processing calendar."""


class UpdateSupplySourceRequestDict(TypedDict):
    supply_source_code: NotRequired[str]
    alias: NotRequired[str]
    node_type: NotRequired[str]
    status: NotRequired[str]
    address: NotRequired[AddressShippingManagementDict]
    configuration: NotRequired[SupplySourceConfigurationDict]
