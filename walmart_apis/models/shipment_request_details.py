from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address1 import Address1, Address1Dict
from .item2 import Item2, Item2Dict
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .shipping_service_options import ShippingServiceOptions, ShippingServiceOptionsDict
from .weight import Weight, WeightDict


class ShipmentRequestDetails(SdkBaseModel):
    purchase_order_id: str = Field(alias="purchaseOrderId")
    """Walmart Purchase Order ID"""

    seller_order_id: Optional[str] = Field(default=UNSET, alias="sellerOrderId")
    item_list: Optional[list[Item2]] = Field(default=UNSET, alias="itemList")
    ship_from_address: Address1 = Field(alias="shipFromAddress")
    ship_to_address: Address1 = Field(alias="shipToAddress")
    package_dimensions: PackageDimensions = Field(alias="packageDimensions")
    weight: Weight
    ship_date: RFC3339DateTime = Field(alias="shipDate")
    shipping_service_options: ShippingServiceOptions = Field(alias="shippingServiceOptions")


class ShipmentRequestDetailsDict(TypedDict):
    purchase_order_id: str
    seller_order_id: NotRequired[str]
    item_list: NotRequired[list[Item2Dict]]
    ship_from_address: Address1Dict
    ship_to_address: Address1Dict
    package_dimensions: PackageDimensionsDict
    weight: WeightDict
    ship_date: RFC3339DateTime
    shipping_service_options: ShippingServiceOptionsDict
