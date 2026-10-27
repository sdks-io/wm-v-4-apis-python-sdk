from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .marketplace_participation import MarketplaceParticipation, MarketplaceParticipationDict


class GetMarketplaceParticipationsResponse(SdkBaseModel):
    payload: Optional[list[MarketplaceParticipation]] = UNSET


class GetMarketplaceParticipationsResponseDict(TypedDict):
    payload: NotRequired[list[MarketplaceParticipationDict]]
