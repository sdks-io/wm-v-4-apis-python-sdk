from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_offers_request import ItemOffersRequest, ItemOffersRequestDict


class GetItemOffersBatchRequest(SdkBaseModel):
    """Request containing Walmart Item ID offer requests for the ``getItemOffersBatch`` operation."""

    requests: Optional[list[ItemOffersRequest]] = UNSET
    """List of ``getItemOffers`` requests to process in a batch. Contains 1–20 requests."""


class GetItemOffersBatchRequestDict(TypedDict):
    requests: NotRequired[list[ItemOffersRequestDict]]
