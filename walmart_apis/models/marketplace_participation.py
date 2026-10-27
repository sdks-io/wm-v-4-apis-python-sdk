from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .marketplace import Marketplace, MarketplaceDict
from .participation import Participation, ParticipationDict


class MarketplaceParticipation(SdkBaseModel):
    marketplace: Optional[Marketplace] = UNSET
    participation: Optional[Participation] = UNSET


class MarketplaceParticipationDict(TypedDict):
    marketplace: NotRequired[MarketplaceDict]
    participation: NotRequired[ParticipationDict]
