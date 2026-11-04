from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_pricing_type import CompetitivePricingType, CompetitivePricingTypeDict
from .identifier_type_product_pricing import IdentifierTypeProductPricing, IdentifierTypeProductPricingDict
from .offer_type_product_pricing import OfferTypeProductPricing, OfferTypeProductPricingDict
from .sales_rank_type import SalesRankType, SalesRankTypeDict


class Product(SdkBaseModel):
    """Pricing, offer, identifier, relationship, and sales information for an item."""

    identifiers: IdentifierTypeProductPricing = Field(alias="Identifiers")
    """Specifies the identifiers used to uniquely identify the item, including the Walmart Marketplace item identifier
    and seller SKU identifier."""

    attribute_sets: Optional[list[Any]] = Field(default=UNSET, alias="AttributeSets")
    """Product attributes returned for the item, when available."""

    relationships: Optional[list[Any]] = Field(default=UNSET, alias="Relationships")
    """Product variation information returned for the item, when applicable."""

    competitive_pricing: Optional[CompetitivePricingType] = Field(default=UNSET, alias="CompetitivePricing")
    """Competitive prices and offer-listing counts for the item."""

    sales_rankings: Optional[list[SalesRankType]] = Field(default=UNSET, alias="SalesRankings")
    """Sales rank information for the item, by category."""

    offers: Optional[list[OfferTypeProductPricing]] = Field(default=UNSET, alias="Offers")
    """Offers returned for the item."""


class ProductDict(TypedDict):
    identifiers: IdentifierTypeProductPricingDict
    attribute_sets: NotRequired[list[Any]]
    relationships: NotRequired[list[Any]]
    competitive_pricing: NotRequired[CompetitivePricingTypeDict]
    sales_rankings: NotRequired[list[SalesRankTypeDict]]
    offers: NotRequired[list[OfferTypeProductPricingDict]]
