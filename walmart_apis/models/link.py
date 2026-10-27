from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Link(SdkBaseModel):
    resource: str
    """URI to resolve the restriction (e.g. approval request URL)"""

    verb: Literal["GET"] = "GET"
    title: Optional[str] = UNSET
    type_: Optional[str] = Field(default=UNSET, alias="type")


class LinkDict(TypedDict):
    resource: str
    verb: Literal["GET"]
    title: NotRequired[str]
    type_: NotRequired[str]
