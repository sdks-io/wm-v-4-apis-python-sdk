from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.seller_status import SellerStatusOrStr


class Participation(SdkBaseModel):
    is_participating: Optional[bool] = Field(default=UNSET, alias="isParticipating")
    has_suspended_listings: Optional[bool] = Field(default=UNSET, alias="hasSuspendedListings")
    seller_status: Optional[SellerStatusOrStr] = Field(default=UNSET, alias="sellerStatus")


class ParticipationDict(TypedDict):
    is_participating: NotRequired[bool]
    has_suspended_listings: NotRequired[bool]
    seller_status: NotRequired[SellerStatusOrStr]
