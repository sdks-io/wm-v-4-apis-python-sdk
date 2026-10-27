from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.name import NameOrStr


class ResearchingQuantityEntry(SdkBaseModel):
    name: Optional[NameOrStr] = UNSET
    """Duration category of the investigation."""

    quantity: Optional[int] = UNSET
    """Number of units in this investigation duration category."""


class ResearchingQuantityEntryDict(TypedDict):
    name: NotRequired[NameOrStr]
    quantity: NotRequired[int]
