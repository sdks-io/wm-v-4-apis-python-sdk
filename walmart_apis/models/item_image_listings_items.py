from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemImageListingsItems(SdkBaseModel):
    link: Optional[str] = UNSET
    height: Optional[int] = UNSET
    width: Optional[int] = UNSET


class ItemImageListingsItemsDict(TypedDict):
    link: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
