from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_address import CommonAddress, CommonAddressDict


class CommonShipmentDestination(SdkBaseModel):
    """The Walmart Ship Node address and warehouse ID."""

    address: Optional[CommonAddress] = UNSET
    """Specific details to identify a place."""

    destination_type: str = Field(alias="destinationType")
    """The type of destination for this shipment. Possible values: ``WALMART_OPTIMIZED``, ``WALMART_SHIP_NODE``."""

    warehouse_id: Optional[str] = Field(default=UNSET, alias="warehouseId")
    """The Ship Node that the shipment should be sent to. This can be empty if the destination type is
    ``WALMART_OPTIMIZED``."""


class CommonShipmentDestinationDict(TypedDict):
    address: NotRequired[CommonAddressDict]
    destination_type: str
    warehouse_id: NotRequired[str]
