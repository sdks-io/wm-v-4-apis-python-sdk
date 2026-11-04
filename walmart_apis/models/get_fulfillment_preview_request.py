from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .address_fulfillment_outbound_wfs import AddressFulfillmentOutboundWfs, AddressFulfillmentOutboundWfsDict
from .enums.shipping_speed_category import ShippingSpeedCategoryOrStr
from .get_fulfillment_preview_item import GetFulfillmentPreviewItem, GetFulfillmentPreviewItemDict


class GetFulfillmentPreviewRequest(SdkBaseModel):
    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    address: AddressFulfillmentOutboundWfs
    items: list[GetFulfillmentPreviewItem]
    shipping_speed_categories: Optional[list[ShippingSpeedCategoryOrStr]] = Field(
        default=UNSET, alias="shippingSpeedCategories"
    )
    include_cod_fulfillment_preview: bool = Field(default=False, alias="includeCODFulfillmentPreview")


class GetFulfillmentPreviewRequestDict(TypedDict):
    marketplace_id: NotRequired[str]
    address: AddressFulfillmentOutboundWfsDict
    items: list[GetFulfillmentPreviewItemDict]
    shipping_speed_categories: NotRequired[list[ShippingSpeedCategoryOrStr]]
    include_cod_fulfillment_preview: NotRequired[bool]
