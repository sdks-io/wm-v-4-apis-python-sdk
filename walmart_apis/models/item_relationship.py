from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .related_item import RelatedItem, RelatedItemDict
from .variation_theme import VariationTheme, VariationThemeDict


class ItemRelationship(SdkBaseModel):
    """Relationship information between catalog items."""

    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    """Type of relationship, such as ``VARIATION``, ``ACCESSORY``, or ``BUNDLE_COMPONENT``."""

    child_items: Optional[list[RelatedItem]] = Field(default=UNSET, alias="childItems")
    parent_items: Optional[list[RelatedItem]] = Field(default=UNSET, alias="parentItems")
    variation_theme: Optional[VariationTheme] = Field(default=UNSET, alias="variationTheme")
    """Attributes used to distinguish product variations, such as color and size."""


class ItemRelationshipDict(TypedDict):
    type_: NotRequired[TypeOrStr]
    child_items: NotRequired[list[RelatedItemDict]]
    parent_items: NotRequired[list[RelatedItemDict]]
    variation_theme: NotRequired[VariationThemeDict]
