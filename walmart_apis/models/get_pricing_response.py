from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_catalog_items import ErrorCatalogItems, ErrorCatalogItemsDict
from .price import Price, PriceDict


class GetPricingResponse(SdkBaseModel):
    """Response schema for ``getPricing`` and ``getCompetitivePricing`` operations."""

    payload: Optional[list[Price]] = UNSET
    """Payload for ``getPricing`` and ``getCompetitivePricing`` operations."""

    errors: Optional[list[ErrorCatalogItems]] = UNSET
    """Error responses returned when a request is unsuccessful."""


class GetPricingResponseDict(TypedDict):
    payload: NotRequired[list[PriceDict]]
    errors: NotRequired[list[ErrorCatalogItemsDict]]
