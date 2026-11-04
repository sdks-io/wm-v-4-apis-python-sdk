from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemAttribute(SdkBaseModel):
    """Value and language information for a product attribute."""

    display_value: Optional[str] = Field(default=UNSET, alias="displayValue")
    """Human-readable value of the product attribute."""

    value: Optional[Any] = UNSET
    """Machine-readable value of the product attribute."""

    language: str = "en_US"
    """Language code for the attribute value, such as ``en-US`` or ``fr-CA``."""


class ItemAttributeDict(TypedDict):
    display_value: NotRequired[str]
    value: NotRequired[Any]
    language: NotRequired[str]
