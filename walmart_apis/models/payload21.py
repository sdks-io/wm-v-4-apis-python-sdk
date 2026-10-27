from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address2 import Address2, Address2Dict


class Payload21(SdkBaseModel):
    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    shipping_address: Optional[Address2] = Field(default=UNSET, alias="shippingAddress")


class Payload21Dict(TypedDict):
    purchase_order_id: NotRequired[str]
    shipping_address: NotRequired[Address2Dict]
