from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_offers_response import ItemOffersResponse, ItemOffersResponseDict


class GetItemOffersBatchResponse(SdkBaseModel):
    """Response containing the results returned by the ``getItemOffersBatch`` operation."""

    responses: Optional[list[ItemOffersResponse]] = UNSET
    """List of responses returned for the batched ``getItemOffers`` requests. Contains 1–20 responses."""


class GetItemOffersBatchResponseDict(TypedDict):
    responses: NotRequired[list[ItemOffersResponseDict]]
