from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_offers_request import ItemOffersRequest, ItemOffersRequestDict


class GetItemOffersBatchRequest(SdkBaseModel):
    """The request associated with the getItemOffersBatch API call."""

    requests: Optional[list[ItemOffersRequest]] = UNSET
    """A list of getItemOffers batched requests to run."""


class GetItemOffersBatchRequestDict(TypedDict):
    requests: NotRequired[list[ItemOffersRequestDict]]
