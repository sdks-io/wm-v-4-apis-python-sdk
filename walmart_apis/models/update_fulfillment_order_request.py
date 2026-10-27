from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address import Address, AddressDict
from .enums.shipping_speed_category import ShippingSpeedCategoryOrStr


class UpdateFulfillmentOrderRequest(SdkBaseModel):
    displayable_order_comment: Optional[str] = Field(default=UNSET, alias="displayableOrderComment")
    shipping_speed_category: Optional[ShippingSpeedCategoryOrStr] = Field(default=UNSET, alias="shippingSpeedCategory")
    destination_address: Optional[Address] = Field(default=UNSET, alias="destinationAddress")
    notification_emails: Optional[list[EmailStr]] = Field(default=UNSET, alias="notificationEmails")


class UpdateFulfillmentOrderRequestDict(TypedDict):
    displayable_order_comment: NotRequired[str]
    shipping_speed_category: NotRequired[ShippingSpeedCategoryOrStr]
    destination_address: NotRequired[AddressDict]
    notification_emails: NotRequired[list[EmailStr]]
