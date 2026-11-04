from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address_merchant_fulfillment_seller_fulfilled_labels import (
    AddressMerchantFulfillmentSellerFulfilledLabels,
    AddressMerchantFulfillmentSellerFulfilledLabelsDict,
)
from .enums.shipment_status_merchant_fulfillment_seller_fulfilled_labels import (
    ShipmentStatusMerchantFulfillmentSellerFulfilledLabelsOrStr,
)
from .item_merchant_fulfillment_seller_fulfilled_labels import (
    ItemMerchantFulfillmentSellerFulfilledLabels,
    ItemMerchantFulfillmentSellerFulfilledLabelsDict,
)
from .label import Label, LabelDict
from .money import Money, MoneyDict
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .shipping_service import ShippingService, ShippingServiceDict
from .weight import Weight, WeightDict


class Shipment(SdkBaseModel):
    shipment_id: str = Field(alias="shipmentId")
    order_id: Optional[str] = Field(default=UNSET, alias="orderId")
    seller_order_id: Optional[str] = Field(default=UNSET, alias="sellerOrderId")
    item_list: Optional[list[ItemMerchantFulfillmentSellerFulfilledLabels]] = Field(default=UNSET, alias="itemList")
    ship_from_address: Optional[AddressMerchantFulfillmentSellerFulfilledLabels] = Field(
        default=UNSET, alias="shipFromAddress"
    )
    ship_to_address: Optional[AddressMerchantFulfillmentSellerFulfilledLabels] = Field(
        default=UNSET, alias="shipToAddress"
    )
    package_dimensions: Optional[PackageDimensions] = Field(default=UNSET, alias="packageDimensions")
    weight: Optional[Weight] = UNSET
    insurance: Optional[Money] = UNSET
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    shipping_service: Optional[ShippingService] = Field(default=UNSET, alias="shippingService")
    label: Optional[Label] = UNSET
    shipment_status: ShipmentStatusMerchantFulfillmentSellerFulfilledLabelsOrStr = Field(alias="shipmentStatus")
    created_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdDate")
    last_updated_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdatedDate")


class ShipmentDict(TypedDict):
    shipment_id: str
    order_id: NotRequired[str]
    seller_order_id: NotRequired[str]
    item_list: NotRequired[list[ItemMerchantFulfillmentSellerFulfilledLabelsDict]]
    ship_from_address: NotRequired[AddressMerchantFulfillmentSellerFulfilledLabelsDict]
    ship_to_address: NotRequired[AddressMerchantFulfillmentSellerFulfilledLabelsDict]
    package_dimensions: NotRequired[PackageDimensionsDict]
    weight: NotRequired[WeightDict]
    insurance: NotRequired[MoneyDict]
    shipping_service: NotRequired[ShippingServiceDict]
    label: NotRequired[LabelDict]
    shipment_status: ShipmentStatusMerchantFulfillmentSellerFulfilledLabelsOrStr
    created_date: NotRequired[RFC3339DateTime]
    last_updated_date: NotRequired[RFC3339DateTime]
