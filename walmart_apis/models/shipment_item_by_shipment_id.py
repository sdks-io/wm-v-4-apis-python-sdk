from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipment_item_by_shipment_id_prep_detail import (
    ShipmentItemByShipmentIdPrepDetail,
    ShipmentItemByShipmentIdPrepDetailDict,
)


class ShipmentItemByShipmentId(SdkBaseModel):
    """Item information for a confirmed inbound shipment, looked up directly by shipment identifier (v0 lookup; no
    inboundPlanId required)."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier for a specific SKU (upstream Inbound Order Workflow ``sku``;
    also referred to as ``sellerSku`` in Amazon SP-API-parity contexts)."""

    fnsku: Optional[str] = UNSET
    """Walmart Fulfillment Network SKU (FNSKU) -- a WFS-assigned identifier for this item within the fulfillment
    network. Upstream reuses the legacy ``gtin`` field slot to carry this value (also referred to as
    ``FulfillmentNetworkSKU`` in Amazon SP-API-parity contexts)."""

    quantity_shipped: int = Field(alias="quantityShipped")
    """The quantity of this item shipped."""

    quantity_received: Optional[int] = Field(default=UNSET, alias="quantityReceived")
    """The quantity of this item received at the fulfillment center."""

    quantity_in_case: Optional[int] = Field(default=UNSET, alias="quantityInCase")
    """The item quantity per inner pack / case."""

    release_date: Optional[str] = Field(default=UNSET, alias="releaseDate")
    """Expected delivery date, in ISO 8601 date format with pattern ``YYYY-MM-DD``."""

    prep_details: Optional[list[ShipmentItemByShipmentIdPrepDetail]] = Field(default=UNSET, alias="prepDetails")
    """Preparation instructions for this item. WFS currently supports LABEL and BAG (Polybagging) only."""


class ShipmentItemByShipmentIdDict(TypedDict):
    msku: str
    fnsku: NotRequired[str]
    quantity_shipped: int
    quantity_received: NotRequired[int]
    quantity_in_case: NotRequired[int]
    release_date: NotRequired[str]
    prep_details: NotRequired[list[ShipmentItemByShipmentIdPrepDetailDict]]
