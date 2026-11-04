from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address_merchant_fulfillment_seller_fulfilled_labels import (
    AddressMerchantFulfillmentSellerFulfilledLabels,
    AddressMerchantFulfillmentSellerFulfilledLabelsDict,
)
from .item_merchant_fulfillment_seller_fulfilled_labels import (
    ItemMerchantFulfillmentSellerFulfilledLabels,
    ItemMerchantFulfillmentSellerFulfilledLabelsDict,
)
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .shipping_service_options import ShippingServiceOptions, ShippingServiceOptionsDict
from .weight import Weight, WeightDict


class ShipmentRequestDetails(SdkBaseModel):
    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Walmart Purchase Order ID"""

    seller_order_id: Optional[str] = Field(default=UNSET, alias="sellerOrderId")
    item_list: Optional[list[ItemMerchantFulfillmentSellerFulfilledLabels]] = Field(default=UNSET, alias="itemList")
    ship_from_address: AddressMerchantFulfillmentSellerFulfilledLabels = Field(alias="shipFromAddress")
    ship_to_address: AddressMerchantFulfillmentSellerFulfilledLabels = Field(alias="shipToAddress")
    package_dimensions: PackageDimensions = Field(alias="packageDimensions")
    weight: Weight
    ship_date: RFC3339DateTime = Field(alias="shipDate")
    shipping_service_options: ShippingServiceOptions = Field(alias="shippingServiceOptions")


class ShipmentRequestDetailsDict(TypedDict):
    purchase_order_id: str
    seller_order_id: NotRequired[str]
    item_list: NotRequired[list[ItemMerchantFulfillmentSellerFulfilledLabelsDict]]
    ship_from_address: AddressMerchantFulfillmentSellerFulfilledLabelsDict
    ship_to_address: AddressMerchantFulfillmentSellerFulfilledLabelsDict
    package_dimensions: PackageDimensionsDict
    weight: WeightDict
    ship_date: RFC3339DateTime
    shipping_service_options: ShippingServiceOptionsDict
