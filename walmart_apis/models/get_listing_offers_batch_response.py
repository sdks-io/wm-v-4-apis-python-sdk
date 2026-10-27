from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listing_offers_response import ListingOffersResponse, ListingOffersResponseDict


class GetListingOffersBatchResponse(SdkBaseModel):
    """The response associated with the getListingOffersBatch API call."""

    responses: Optional[list[ListingOffersResponse]] = UNSET
    """A list of getListingOffers batched responses."""


class GetListingOffersBatchResponseDict(TypedDict):
    responses: NotRequired[list[ListingOffersResponseDict]]
