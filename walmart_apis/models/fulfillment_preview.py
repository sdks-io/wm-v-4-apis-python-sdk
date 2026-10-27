from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.shipping_speed_category import ShippingSpeedCategoryOrStr
from .fee import Fee, FeeDict
from .fulfillment_preview_shipment import FulfillmentPreviewShipment, FulfillmentPreviewShipmentDict


class FulfillmentPreview(SdkBaseModel):
    shipping_speed_category: Optional[ShippingSpeedCategoryOrStr] = Field(default=UNSET, alias="shippingSpeedCategory")
    fulfillment_preview_shipments: Optional[list[FulfillmentPreviewShipment]] = Field(
        default=UNSET, alias="fulfillmentPreviewShipments"
    )
    is_fulfillable: Optional[bool] = Field(default=UNSET, alias="isFulfillable")
    is_cod_capable: Optional[bool] = Field(default=UNSET, alias="isCODCapable")
    estimated_fees: Optional[list[Fee]] = Field(default=UNSET, alias="estimatedFees")


class FulfillmentPreviewDict(TypedDict):
    shipping_speed_category: NotRequired[ShippingSpeedCategoryOrStr]
    fulfillment_preview_shipments: NotRequired[list[FulfillmentPreviewShipmentDict]]
    is_fulfillable: NotRequired[bool]
    is_cod_capable: NotRequired[bool]
    estimated_fees: NotRequired[list[FeeDict]]
