from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address import Address, AddressDict
from .enums.fulfillment_order_status import FulfillmentOrderStatusOrStr
from .enums.shipping_speed_category import ShippingSpeedCategoryOrStr


class FulfillmentOrder(SdkBaseModel):
    seller_fulfillment_order_id: str = Field(alias="sellerFulfillmentOrderId")
    """Seller-defined order ID"""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    displayable_order_id: str = Field(alias="displayableOrderId")
    """Order ID shown to the recipient"""

    displayable_order_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="displayableOrderDate")
    displayable_order_comment: Optional[str] = Field(default=UNSET, alias="displayableOrderComment")
    shipping_speed_category: Optional[ShippingSpeedCategoryOrStr] = Field(default=UNSET, alias="shippingSpeedCategory")
    destination_address: Optional[Address] = Field(default=UNSET, alias="destinationAddress")
    fulfillment_order_status: FulfillmentOrderStatusOrStr = Field(alias="fulfillmentOrderStatus")
    status_updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="statusUpdatedAt")
    notification_emails: Optional[list[EmailStr]] = Field(default=UNSET, alias="notificationEmails")


class FulfillmentOrderDict(TypedDict):
    seller_fulfillment_order_id: str
    marketplace_id: NotRequired[str]
    displayable_order_id: str
    displayable_order_date: NotRequired[RFC3339DateTime]
    displayable_order_comment: NotRequired[str]
    shipping_speed_category: NotRequired[ShippingSpeedCategoryOrStr]
    destination_address: NotRequired[AddressDict]
    fulfillment_order_status: FulfillmentOrderStatusOrStr
    status_updated_at: NotRequired[RFC3339DateTime]
    notification_emails: NotRequired[list[EmailStr]]
