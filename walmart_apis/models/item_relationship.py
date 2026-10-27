from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type import TypeOrStr
from .related_item import RelatedItem, RelatedItemDict
from .variation_theme import VariationTheme, VariationThemeDict


class ItemRelationship(SdkBaseModel):
    type_: Optional[TypeOrStr] = Field(default=UNSET, alias="type")
    child_items: Optional[list[RelatedItem]] = Field(default=UNSET, alias="childItems")
    parent_items: Optional[list[RelatedItem]] = Field(default=UNSET, alias="parentItems")
    variation_theme: Optional[VariationTheme] = Field(default=UNSET, alias="variationTheme")


class ItemRelationshipDict(TypedDict):
    type_: NotRequired[TypeOrStr]
    child_items: NotRequired[list[RelatedItemDict]]
    parent_items: NotRequired[list[RelatedItemDict]]
    variation_theme: NotRequired[VariationThemeDict]
