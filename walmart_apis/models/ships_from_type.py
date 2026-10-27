from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ShipsFromType(SdkBaseModel):
    """The state and country from where the item is shipped."""

    state: Optional[str] = Field(default=UNSET, alias="State")
    """The state from where the item is shipped."""

    country: Optional[str] = Field(default=UNSET, alias="Country")
    """The country from where the item is shipped."""


class ShipsFromTypeDict(TypedDict):
    state: NotRequired[str]
    country: NotRequired[str]
