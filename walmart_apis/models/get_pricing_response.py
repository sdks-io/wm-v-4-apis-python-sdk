from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error3 import Error3, Error3Dict
from .price import Price, PriceDict


class GetPricingResponse(SdkBaseModel):
    """The response schema for the getPricing and getCompetitivePricing operations."""

    payload: Optional[list[Price]] = UNSET
    """The payload for the getPricing and getCompetitivePricing operations."""

    errors: Optional[list[Error3]] = UNSET
    """A list of error responses returned when a request is unsuccessful."""


class GetPricingResponseDict(TypedDict):
    payload: NotRequired[list[PriceDict]]
    errors: NotRequired[list[Error3Dict]]
