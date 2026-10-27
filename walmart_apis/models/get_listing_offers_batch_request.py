from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .listing_offers_request import ListingOffersRequest, ListingOffersRequestDict


class GetListingOffersBatchRequest(SdkBaseModel):
    """The request associated with the getListingOffersBatch API call."""

    requests: Optional[list[ListingOffersRequest]] = UNSET
    """A list of getListingOffers batched requests to run."""


class GetListingOffersBatchRequestDict(TypedDict):
    requests: NotRequired[list[ListingOffersRequestDict]]
