from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.variant import VariantOrStr


class ItemImage(SdkBaseModel):
    """Image information for a catalog item."""

    variant: Optional[VariantOrStr] = UNSET
    """Image variant type, such as ``MAIN`` for the primary product image or ``SWCH`` for a color swatch image."""

    link: Optional[str] = UNSET
    """URL of the product image."""

    height: Optional[int] = UNSET
    """Height of the product image in pixels."""

    width: Optional[int] = UNSET
    """Width of the product image in pixels."""


class ItemImageDict(TypedDict):
    variant: NotRequired[VariantOrStr]
    link: NotRequired[str]
    height: NotRequired[int]
    width: NotRequired[int]
