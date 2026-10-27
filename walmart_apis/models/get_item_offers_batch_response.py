from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_offers_response import ItemOffersResponse, ItemOffersResponseDict


class GetItemOffersBatchResponse(SdkBaseModel):
    """The response associated with the getItemOffersBatch API call."""

    responses: Optional[list[ItemOffersResponse]] = UNSET
    """A list of getItemOffers batched responses."""


class GetItemOffersBatchResponseDict(TypedDict):
    responses: NotRequired[list[ItemOffersResponseDict]]
