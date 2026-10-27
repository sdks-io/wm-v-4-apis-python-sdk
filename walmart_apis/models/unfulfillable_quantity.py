from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UnfulfillableQuantity(SdkBaseModel):
    """Breakdown of units that cannot be fulfilled."""

    total_unfulfillable_quantity: OptionalNullable[int] = Field(default=UNSET, alias="totalUnfulfillableQuantity")
    """Total units that cannot be fulfilled."""

    customer_damaged_quantity: OptionalNullable[int] = Field(default=UNSET, alias="customerDamagedQuantity")
    """Units damaged by a customer return."""

    warehouse_damaged_quantity: OptionalNullable[int] = Field(default=UNSET, alias="warehouseDamagedQuantity")
    """Units damaged in the fulfillment center."""

    distributor_damaged_quantity: OptionalNullable[int] = Field(default=UNSET, alias="distributorDamagedQuantity")
    """Units damaged by the distributor."""

    carrier_damaged_quantity: OptionalNullable[int] = Field(default=UNSET, alias="carrierDamagedQuantity")
    """Units damaged in transit by a carrier."""

    defective_quantity: OptionalNullable[int] = Field(default=UNSET, alias="defectiveQuantity")
    """Units identified as defective."""

    expired_quantity: OptionalNullable[int] = Field(default=UNSET, alias="expiredQuantity")
    """Units that have passed their expiration date."""


class UnfulfillableQuantityDict(TypedDict):
    total_unfulfillable_quantity: NotRequired[int | None]
    customer_damaged_quantity: NotRequired[int | None]
    warehouse_damaged_quantity: NotRequired[int | None]
    distributor_damaged_quantity: NotRequired[int | None]
    carrier_damaged_quantity: NotRequired[int | None]
    defective_quantity: NotRequired[int | None]
    expired_quantity: NotRequired[int | None]
