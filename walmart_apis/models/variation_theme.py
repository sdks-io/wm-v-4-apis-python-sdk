from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class VariationTheme(SdkBaseModel):
    """Attributes used to distinguish product variations, such as color and size."""

    attributes: Optional[list[str]] = UNSET
    """Attributes used to distinguish variations, such as color and size."""


class VariationThemeDict(TypedDict):
    attributes: NotRequired[list[str]]
