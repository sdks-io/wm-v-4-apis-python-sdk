from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listing_offers_request import ListingOffersRequest, ListingOffersRequestDict


class GetListingOffersBatchRequest(SdkBaseModel):
    """Request containing listing-offer requests for the ``getListingOffersBatch`` operation."""

    requests: Optional[list[ListingOffersRequest]] = UNSET
    """List of ``getListingOffers`` requests to process in a batch. Contains 1–20 requests."""


class GetListingOffersBatchRequestDict(TypedDict):
    requests: NotRequired[list[ListingOffersRequestDict]]
