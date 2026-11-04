from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class BuyboxOfferExpectedPriceRequest(SdkBaseModel):
    """Buybox offer expected price (BOEP) request for a specific seller SKU. Does not carry a marketplaceId -- the
    marketplace is resolved from the gateway-derived tenant context (x-o-tenant), same as every other pricing endpoint.
    See PricingValidation#currentMarketplaceId."""

    sku: str
    """Seller stock keeping unit (SKU) that identifies the item."""


class BuyboxOfferExpectedPriceRequestDict(TypedDict):
    sku: str
