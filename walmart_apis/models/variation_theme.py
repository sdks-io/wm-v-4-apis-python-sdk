from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VariationTheme(SdkBaseModel):
    attributes: Optional[list[str]] = UNSET


class VariationThemeDict(TypedDict):
    attributes: NotRequired[list[str]]
