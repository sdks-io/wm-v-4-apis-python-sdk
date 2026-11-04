from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_shipping_management import AddressShippingManagement, AddressShippingManagementDict
from .supply_source_configuration import SupplySourceConfiguration, SupplySourceConfigurationDict


class SupplySource(SdkBaseModel):
    supply_source_id: Optional[str] = Field(default=UNSET, alias="supplySourceId")
    """Unique identifier for the supply source."""

    supply_source_code: Optional[str] = Field(default=UNSET, alias="supplySourceCode")
    """Human-readable code for the supply source."""

    alias: Optional[str] = UNSET
    """Custom alias for the supply source."""

    node_type: Optional[str] = Field(default=UNSET, alias="nodeType")
    """Type of node. Known values today: PHYSICAL, VIRTUAL, 3PL."""

    status: Optional[str] = UNSET
    """Current status of the supply source. Known values today: ACTIVE, INACTIVE."""

    address: Optional[AddressShippingManagement] = UNSET
    """A postal address. Canonical shared shape -- see com.walmart.seller.core.model.Address's Javadoc (seller-api-core)
    for the full rationale and per-field examples."""

    configuration: Optional[SupplySourceConfiguration] = UNSET
    """Operating settings for the supply source — time zone and the processing calendar."""


class SupplySourceDict(TypedDict):
    supply_source_id: NotRequired[str]
    supply_source_code: NotRequired[str]
    alias: NotRequired[str]
    node_type: NotRequired[str]
    status: NotRequired[str]
    address: NotRequired[AddressShippingManagementDict]
    configuration: NotRequired[SupplySourceConfigurationDict]
