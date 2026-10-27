from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.reason_code import ReasonCodeOrStr
from .link import Link, LinkDict


class Reason(SdkBaseModel):
    message: str
    """Localized human-readable message explaining the restriction"""

    reason_code: ReasonCodeOrStr = Field(alias="reasonCode")
    links: Optional[list[Link]] = UNSET


class ReasonDict(TypedDict):
    message: str
    reason_code: ReasonCodeOrStr
    links: NotRequired[list[LinkDict]]
