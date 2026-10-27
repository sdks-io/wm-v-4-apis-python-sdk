from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.severity import SeverityOrStr


class Issue(SdkBaseModel):
    code: str
    """Machine-readable issue code"""

    message: str
    """Human-readable issue message (locale-aware)"""

    severity: SeverityOrStr
    attribute_names: Optional[list[str]] = Field(default=UNSET, alias="attributeNames")
    """Affected attribute names"""


class IssueDict(TypedDict):
    code: str
    message: str
    severity: SeverityOrStr
    attribute_names: NotRequired[list[str]]
