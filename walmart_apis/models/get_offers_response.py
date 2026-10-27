from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict
from .get_offers_result import GetOffersResult, GetOffersResultDict


class GetOffersResponse(SdkBaseModel):
    """The response schema for the getListingOffers and getItemOffers operations."""

    payload: Optional[GetOffersResult] = UNSET
    """The payload for the getListingOffers and getItemOffers operations."""

    errors: Optional[list[Error3]] = UNSET
    """A list of error responses returned when a request is unsuccessful."""


class GetOffersResponseDict(TypedDict):
    payload: NotRequired[GetOffersResultDict]
    errors: NotRequired[list[Error3Dict]]
