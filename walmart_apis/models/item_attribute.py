from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ItemAttribute(SdkBaseModel):
    display_value: Optional[str] = Field(default=UNSET, alias="displayValue")
    value: Optional[Any] = UNSET
    language: str = "en_US"


class ItemAttributeDict(TypedDict):
    display_value: NotRequired[str]
    value: NotRequired[Any]
    language: NotRequired[str]
