from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_type_product_pricing import FulfillmentTypeProductPricingOrStr


class OfferIdentifier(SdkBaseModel):
    """Identifies an offer by marketplace, seller, seller SKU, and fulfillment type."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """Walmart Marketplace identifier associated with the offer."""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """Seller identifier associated with the offer."""

    sku: Optional[str] = UNSET
    """Seller stock keeping unit (SKU) that identifies the item."""

    fulfillment_type: Optional[FulfillmentTypeProductPricingOrStr] = Field(default=UNSET, alias="fulfillmentType")
    """Fulfillment type for the offer. Possible values are ``WFS`` and ``SELLER``."""


class OfferIdentifierDict(TypedDict):
    marketplace_id: NotRequired[str]
    seller_id: NotRequired[str]
    sku: NotRequired[str]
    fulfillment_type: NotRequired[FulfillmentTypeProductPricingOrStr]
