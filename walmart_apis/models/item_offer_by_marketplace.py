from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.offer_type import OfferTypeOrStr
from .money import Money, MoneyDict
from .points import Points, PointsDict


class ItemOfferByMarketplace(SdkBaseModel):
    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    offer_type: Optional[OfferTypeOrStr] = Field(default=UNSET, alias="offerType")
    price: Optional[Money] = UNSET
    points: Optional[Points] = UNSET


class ItemOfferByMarketplaceDict(TypedDict):
    marketplace_id: NotRequired[str]
    offer_type: NotRequired[OfferTypeOrStr]
    price: NotRequired[MoneyDict]
    points: NotRequired[PointsDict]
