from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .researching_quantity import ResearchingQuantity, ResearchingQuantityDict
from .reserved_quantity import ReservedQuantity, ReservedQuantityDict
from .unfulfillable_quantity import UnfulfillableQuantity, UnfulfillableQuantityDict


class InventoryDetails(SdkBaseModel):
    """Inventory quantity breakdown for a SKU at a ship node."""

    fulfillable_quantity: OptionalNullable[int] = Field(default=UNSET, alias="fulfillableQuantity")
    """Units currently available to sell at this ship node. Null if the upstream quantity is unavailable."""

    on_hand_quantity: OptionalNullable[int] = Field(default=UNSET, alias="onHandQuantity")
    """Total units physically at this ship node, including available, reserved, and unfulfillable units. Null if
    unavailable."""

    reserved_quantity: Optional[ReservedQuantity] = Field(default=UNSET, alias="reservedQuantity")
    """Breakdown of reserved quantities."""

    researching_quantity: OptionalNullable[ResearchingQuantity] = Field(default=UNSET, alias="researchingQuantity")
    """Units currently under investigation for discrepancies between expected and physical on-hand counts. Null if no
    units are under investigation."""

    unfulfillable_quantity: OptionalNullable[UnfulfillableQuantity] = Field(
        default=UNSET, alias="unfulfillableQuantity"
    )
    """Units that cannot be fulfilled due to damage, defects, or expiry. Null if no unfulfillable units exist."""

    inbound_working_quantity: OptionalNullable[int] = Field(default=UNSET, alias="inboundWorkingQuantity")
    """Units for which a shipment has been created but not yet shipped. Null if no data is available."""

    inbound_shipped_quantity: OptionalNullable[int] = Field(default=UNSET, alias="inboundShippedQuantity")
    """Units that have been shipped to the fulfillment center but not yet received. Null if no data is available."""

    inbound_receiving_quantity: OptionalNullable[int] = Field(default=UNSET, alias="inboundReceivingQuantity")
    """Units that are being received at the fulfillment center. Null if no data is available."""


class InventoryDetailsDict(TypedDict):
    fulfillable_quantity: NotRequired[int | None]
    on_hand_quantity: NotRequired[int | None]
    reserved_quantity: NotRequired[ReservedQuantityDict]
    researching_quantity: NotRequired[ResearchingQuantityDict | None]
    unfulfillable_quantity: NotRequired[UnfulfillableQuantityDict | None]
    inbound_working_quantity: NotRequired[int | None]
    inbound_shipped_quantity: NotRequired[int | None]
    inbound_receiving_quantity: NotRequired[int | None]
