from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address1 import Address1, Address1Dict
from .enums.shipment_status import ShipmentStatusOrStr
from .item2 import Item2, Item2Dict
from .label import Label, LabelDict
from .money import Money, MoneyDict
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .shipping_service import ShippingService, ShippingServiceDict
from .weight import Weight, WeightDict


class Shipment(SdkBaseModel):
    shipment_id: str = Field(alias="shipmentId")
    order_id: Optional[str] = Field(default=UNSET, alias="orderId")
    seller_order_id: Optional[str] = Field(default=UNSET, alias="sellerOrderId")
    item_list: Optional[list[Item2]] = Field(default=UNSET, alias="itemList")
    ship_from_address: Optional[Address1] = Field(default=UNSET, alias="shipFromAddress")
    ship_to_address: Optional[Address1] = Field(default=UNSET, alias="shipToAddress")
    package_dimensions: Optional[PackageDimensions] = Field(default=UNSET, alias="packageDimensions")
    weight: Optional[Weight] = UNSET
    insurance: Optional[Money] = UNSET
    shipping_service: Optional[ShippingService] = Field(default=UNSET, alias="shippingService")
    label: Optional[Label] = UNSET
    shipment_status: ShipmentStatusOrStr = Field(alias="shipmentStatus")
    created_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdDate")
    last_updated_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="lastUpdatedDate")


class ShipmentDict(TypedDict):
    shipment_id: str
    order_id: NotRequired[str]
    seller_order_id: NotRequired[str]
    item_list: NotRequired[list[Item2Dict]]
    ship_from_address: NotRequired[Address1Dict]
    ship_to_address: NotRequired[Address1Dict]
    package_dimensions: NotRequired[PackageDimensionsDict]
    weight: NotRequired[WeightDict]
    insurance: NotRequired[MoneyDict]
    shipping_service: NotRequired[ShippingServiceDict]
    label: NotRequired[LabelDict]
    shipment_status: ShipmentStatusOrStr
    created_date: NotRequired[RFC3339DateTime]
    last_updated_date: NotRequired[RFC3339DateTime]
