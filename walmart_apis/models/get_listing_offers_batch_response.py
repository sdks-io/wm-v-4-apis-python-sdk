from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listing_offers_response import ListingOffersResponse, ListingOffersResponseDict


class GetListingOffersBatchResponse(SdkBaseModel):
    """Response containing the results returned by the ``getListingOffersBatch`` operation."""

    responses: Optional[list[ListingOffersResponse]] = UNSET
    """List of responses returned for the batched ``getListingOffers`` requests. Contains 1–20 responses."""


class GetListingOffersBatchResponseDict(TypedDict):
    responses: NotRequired[list[ListingOffersResponseDict]]
