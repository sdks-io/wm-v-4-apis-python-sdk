from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .shipment_item_prep_detail import ShipmentItemPrepDetail, ShipmentItemPrepDetailDict


class ShipmentItem(SdkBaseModel):
    """Item information for a shipment, as returned by ``getShipmentItems`` (aligned with the Inbound Order Workflow
    upstream ``ShipmentItem`` shape)."""

    shipment_id: Optional[str] = Field(default=UNSET, alias="shipmentId")
    """The shipment this item row belongs to (upstream ShipmentId)."""

    seller_sku: str = Field(alias="sellerSku")
    """The seller's SKU for this item (upstream sku; Amazon SP-API-parity name SellerSKU)."""

    fulfillment_network_sku: Optional[str] = Field(default=UNSET, alias="fulfillmentNetworkSKU")
    """Walmart Fulfillment Network SKU for this item (upstream reuses the legacy ``gtin`` field slot to carry this
    value; Amazon SP-API-parity name FulfillmentNetworkSKU)."""

    quantity_shipped: Optional[int] = Field(default=UNSET, alias="quantityShipped")
    """Quantity of this item shipped (upstream QuantityShipped)."""

    quantity_received: Optional[int] = Field(default=UNSET, alias="quantityReceived")
    """Quantity of this item received (upstream QuantityReceived)."""

    quantity_in_case: Optional[int] = Field(default=UNSET, alias="quantityInCase")
    """Quantity of this item per inner pack/case (upstream QuantityInCase)."""

    release_date: Optional[str] = Field(default=UNSET, alias="releaseDate")
    """Release date, ISO 8601 date format YYYY-MM-DD (upstream ReleaseDate)."""

    prep_details: Optional[list[ShipmentItemPrepDetail]] = Field(default=UNSET, alias="prepDetails")
    """Preparation instructions for this item (upstream PrepDetailsList)."""


class ShipmentItemDict(TypedDict):
    shipment_id: NotRequired[str]
    seller_sku: str
    fulfillment_network_sku: NotRequired[str]
    quantity_shipped: NotRequired[int]
    quantity_received: NotRequired[int]
    quantity_in_case: NotRequired[int]
    release_date: NotRequired[str]
    prep_details: NotRequired[list[ShipmentItemPrepDetailDict]]
