from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class ReservedQuantity(SdkBaseModel):
    """Breakdown of reserved quantities."""

    total_reserved_quantity: OptionalNullable[int] = Field(default=UNSET, alias="totalReservedQuantity")
    """Total units reserved across all reservation types."""

    pending_customer_order_quantity: OptionalNullable[int] = Field(default=UNSET, alias="pendingCustomerOrderQuantity")
    """Units reserved for pending customer orders. Null if no breakdown data is available."""

    pending_transshipment_quantity: OptionalNullable[int] = Field(default=UNSET, alias="pendingTransshipmentQuantity")
    """Units reserved for pending transfers between fulfillment centers. Null if no breakdown data is available."""

    fc_processing_quantity: OptionalNullable[int] = Field(default=UNSET, alias="fcProcessingQuantity")
    """Units being processed at the fulfillment center (e.g. receiving, labeling). Null if no data is available."""


class ReservedQuantityDict(TypedDict):
    total_reserved_quantity: NotRequired[int | None]
    pending_customer_order_quantity: NotRequired[int | None]
    pending_transshipment_quantity: NotRequired[int | None]
    fc_processing_quantity: NotRequired[int | None]
