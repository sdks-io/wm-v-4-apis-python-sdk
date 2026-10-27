from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel
from .enums.item_lifecycle import ItemLifecycleOrStr
from .enums.publishing_status import PublishingStatusOrStr
from .enums.stock_status import StockStatusOrStr
from .researching_quantity import ResearchingQuantity, ResearchingQuantityDict
from .reserved_quantity import ReservedQuantity, ReservedQuantityDict
from .unfulfillable_quantity import UnfulfillableQuantity, UnfulfillableQuantityDict
from .wfs_inventory_age import WfsInventoryAge, WfsInventoryAgeDict
from .wfs_unavailable_quantity import WfsUnavailableQuantity, WfsUnavailableQuantityDict


class WfsInventoryDetails(SdkBaseModel):
    publishing_status: Optional[PublishingStatusOrStr] = Field(default=UNSET, alias="publishingStatus")
    """Current listing state of the item on Walmart.com."""

    item_lifecycle: Optional[ItemLifecycleOrStr] = Field(default=UNSET, alias="itemLifecycle")
    """Lifecycle state of the item in the Walmart catalog."""

    stock_status: Optional[StockStatusOrStr] = Field(default=UNSET, alias="stockStatus")
    """Stock health label based on current days of supply."""

    fulfillable_quantity: Optional[int] = Field(default=UNSET, alias="fulfillableQuantity")
    """Units currently available to sell."""

    reserved_quantity: OptionalNullable[ReservedQuantity] = Field(default=UNSET, alias="reservedQuantity")
    """Units reserved and not available for immediate sale. Null if no breakdown data is available."""

    inbound_quantity: Optional[int] = Field(default=UNSET, alias="inboundQuantity")
    """Units currently in transit and not yet available to sell."""

    on_hand_quantity: Optional[int] = Field(default=UNSET, alias="onHandQuantity")
    """Total units physically at fulfillment centers, including available, reserved, and unavailable units."""

    unavailable_quantity: Optional[WfsUnavailableQuantity] = Field(default=UNSET, alias="unavailableQuantity")
    researching_quantity: OptionalNullable[ResearchingQuantity] = Field(default=UNSET, alias="researchingQuantity")
    """Units under investigation for inventory discrepancies. Null if no units are under investigation."""

    unfulfillable_quantity: OptionalNullable[UnfulfillableQuantity] = Field(
        default=UNSET, alias="unfulfillableQuantity"
    )
    """Units that cannot be fulfilled due to damage, defects, or expiry. Null if no unfulfillable units exist."""

    inventory_age: Optional[WfsInventoryAge] = Field(default=UNSET, alias="inventoryAge")
    """Units grouped by storage duration. Used for long-term storage fee assessment. 7 buckets: days365Plus,
    days365To450, and days450Plus reflect the upstream split-aged-buckets feature — days365Plus is the pre-split
    total."""

    first_in_stock_date: OptionalNullable[Date] = Field(default=UNSET, alias="firstInStockDate")
    """Date item first arrived at a fulfillment center. Null if not yet received."""


class WfsInventoryDetailsDict(TypedDict):
    publishing_status: NotRequired[PublishingStatusOrStr]
    item_lifecycle: NotRequired[ItemLifecycleOrStr]
    stock_status: NotRequired[StockStatusOrStr]
    fulfillable_quantity: NotRequired[int]
    reserved_quantity: NotRequired[ReservedQuantityDict | None]
    inbound_quantity: NotRequired[int]
    on_hand_quantity: NotRequired[int]
    unavailable_quantity: NotRequired[WfsUnavailableQuantityDict]
    researching_quantity: NotRequired[ResearchingQuantityDict | None]
    unfulfillable_quantity: NotRequired[UnfulfillableQuantityDict | None]
    inventory_age: NotRequired[WfsInventoryAgeDict]
    first_in_stock_date: NotRequired[Date | None]
