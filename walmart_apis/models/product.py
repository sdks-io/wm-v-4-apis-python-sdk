from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .competitive_pricing_type import CompetitivePricingType, CompetitivePricingTypeDict
from .identifier_type1 import IdentifierType1, IdentifierType1Dict
from .offer_type1 import OfferType1, OfferType1Dict
from .sales_rank_type import SalesRankType, SalesRankTypeDict


class Product(SdkBaseModel):
    """An item."""

    identifiers: IdentifierType1 = Field(alias="Identifiers")
    """Specifies the identifiers used to uniquely identify an item."""

    attribute_sets: Optional[list[Any]] = Field(default=UNSET, alias="AttributeSets")
    """A list of product attributes if applicable."""

    relationships: Optional[list[Any]] = Field(default=UNSET, alias="Relationships")
    """A list that contains product variation information, if applicable."""

    competitive_pricing: Optional[CompetitivePricingType] = Field(default=UNSET, alias="CompetitivePricing")
    """Competitive pricing information for the item."""

    sales_rankings: Optional[list[SalesRankType]] = Field(default=UNSET, alias="SalesRankings")
    """A list of sales rank information for the item, by category."""

    offers: Optional[list[OfferType1]] = Field(default=UNSET, alias="Offers")
    """A list of offers."""


class ProductDict(TypedDict):
    identifiers: IdentifierType1Dict
    attribute_sets: NotRequired[list[Any]]
    relationships: NotRequired[list[Any]]
    competitive_pricing: NotRequired[CompetitivePricingTypeDict]
    sales_rankings: NotRequired[list[SalesRankTypeDict]]
    offers: NotRequired[list[OfferType1Dict]]
