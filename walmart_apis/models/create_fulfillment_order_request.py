from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address import Address, AddressDict
from .create_fulfillment_order_item import CreateFulfillmentOrderItem, CreateFulfillmentOrderItemDict
from .enums.shipping_speed_category import ShippingSpeedCategoryOrStr


class CreateFulfillmentOrderRequest(SdkBaseModel):
    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    seller_fulfillment_order_id: str = Field(alias="sellerFulfillmentOrderId")
    displayable_order_id: str = Field(alias="displayableOrderId")
    displayable_order_date: RFC3339DateTime = Field(alias="displayableOrderDate")
    displayable_order_comment: Optional[str] = Field(default=UNSET, alias="displayableOrderComment")
    shipping_speed_category: ShippingSpeedCategoryOrStr = Field(alias="shippingSpeedCategory")
    destination_address: Address = Field(alias="destinationAddress")
    items: list[CreateFulfillmentOrderItem]
    notification_emails: Optional[list[EmailStr]] = Field(default=UNSET, alias="notificationEmails")


class CreateFulfillmentOrderRequestDict(TypedDict):
    marketplace_id: NotRequired[str]
    seller_fulfillment_order_id: str
    displayable_order_id: str
    displayable_order_date: RFC3339DateTime
    displayable_order_comment: NotRequired[str]
    shipping_speed_category: ShippingSpeedCategoryOrStr
    destination_address: AddressDict
    items: list[CreateFulfillmentOrderItemDict]
    notification_emails: NotRequired[list[EmailStr]]
