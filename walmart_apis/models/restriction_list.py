from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .restriction import Restriction, RestrictionDict


class RestrictionList(SdkBaseModel):
    restrictions: Optional[list[Restriction]] = UNSET


class RestrictionListDict(TypedDict):
    restrictions: NotRequired[list[RestrictionDict]]
