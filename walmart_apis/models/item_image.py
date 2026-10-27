from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.variant import VariantOrStr


class ItemImage(SdkBaseModel):
    variant: Optional[VariantOrStr] = UNSET
    link: Optional[str] = UNSET
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET


class ItemImageDict(TypedDict):
    variant: NotRequired[VariantOrStr]
    link: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
