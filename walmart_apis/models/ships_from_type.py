from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShipsFromType(SdkBaseModel):
    """State and country from which the item ships."""

    state: Optional[str] = Field(default=UNSET, alias="State")
    """State from which the item ships."""

    country: Optional[str] = Field(default=UNSET, alias="Country")
    """Country from which the item ships."""


class ShipsFromTypeDict(TypedDict):
    state: NotRequired[str]
    country: NotRequired[str]
