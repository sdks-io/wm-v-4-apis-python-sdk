from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .money import Money, MoneyDict


class Fee(SdkBaseModel):
    name: Optional[str] = UNSET
    amount: Optional[Money] = UNSET


class FeeDict(TypedDict):
    name: NotRequired[str]
    amount: NotRequired[MoneyDict]
