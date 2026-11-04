from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_catalog_items import ErrorCatalogItems, ErrorCatalogItemsDict
from .get_offers_result import GetOffersResult, GetOffersResultDict


class GetOffersResponse(SdkBaseModel):
    """Response schema for ``getListingOffers`` and ``getItemOffers`` operations."""

    payload: Optional[GetOffersResult] = UNSET
    """Offer results returned by the ``getListingOffers`` and ``getItemOffers`` operations, including summary pricing
    and individual offers."""

    errors: Optional[list[ErrorCatalogItems]] = UNSET
    """Error responses returned when a request is unsuccessful."""


class GetOffersResponseDict(TypedDict):
    payload: NotRequired[GetOffersResultDict]
    errors: NotRequired[list[ErrorCatalogItemsDict]]
